// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/access/AccessControl.sol";

contract AgroTrace is AccessControl {
    bytes32 public constant FARMER_ROLE = keccak256("FARMER_ROLE");
    bytes32 public constant COLLECTOR_ROLE = keccak256("COLLECTOR_ROLE");
    bytes32 public constant WAREHOUSE_ROLE = keccak256("WAREHOUSE_ROLE");
    bytes32 public constant GRADER_ROLE = keccak256("GRADER_ROLE");
    bytes32 public constant PROCESSOR_ROLE = keccak256("PROCESSOR_ROLE");
    bytes32 public constant AUDITOR_ROLE = keccak256("AUDITOR_ROLE");

    uint8 public constant LOSS_MOISTURE = 0;
    uint8 public constant LOSS_TRANSPORT = 1;
    uint8 public constant LOSS_STORAGE = 2;
    uint8 public constant LOSS_SPILLAGE = 3;

    uint256 public constant TOLERANCE_MOISTURE_BPS = 300;
    uint256 public constant TOLERANCE_TRANSPORT_BPS = 100;
    uint256 public constant TOLERANCE_STORAGE_BPS = 150;
    uint256 public constant TOLERANCE_SPILLAGE_BPS = 50;

    enum LotStatus { CREATED, IN_TRANSIT, RECEIVED, GRADED, ALLOCATED, SETTLED, DISPUTED }

    struct Lot {
        uint256 id;
        uint256[] parentIds;
        address owner;
        string cropId;
        uint256 weightG;
        uint256 lossG;
        uint8 lossReason;
        uint256 gradeAttId;
        LotStatus status;
        uint256 allocatedWeightG;
    }

    struct GradeAttestation {
        uint256 id;
        uint256 lotId;
        uint8 grade;
        uint256 moistureBps;
        uint256 impurityBps;
        string evidenceCid;
        bytes32 evidenceSha256;
        address grader;
        uint256 timestamp;
    }

    struct ProcurementContract {
        uint256 id;
        address processor;
        string cropId;
        uint256 qtyG;
        uint8 minGrade;
        uint256 basePricePerKgPaise;
        uint256[3] gradeMultiplierBps;
        uint256 deadline;
        uint256 shortfallPenaltyPaise;
        uint256 allocatedQtyG;
        bool active;
    }

    struct Claim {
        uint256 claimId;
        uint256 lotId;
        string invoiceId;
        uint256 amountPaise;
        address claimant;
        bool settled;
        bool rejected;
    }

    uint256 public lotCounter;
    uint256 public gradeCounter;
    uint256 public contractCounter;
    bytes32 public auditHead;

    mapping(uint256 => Lot) public lots;
    mapping(uint256 => uint256[]) private _childLotIds;
    mapping(uint256 => GradeAttestation) public gradeAttestations;
    mapping(uint256 => ProcurementContract) public contracts;
    mapping(uint256 => Claim) public claims;

    mapping(uint256 => bool) public lotSettled;
    mapping(string => bool) public usedInvoices;
    mapping(address => mapping(uint256 => bool)) public usedNonces;

    error UnauthorizedRole(bytes32 expectedRole, address account);
    error NotLotOwner(uint256 lotId, address caller);
    error LotNotFound(uint256 lotId);
    error LossAboveTolerance(uint256 lossBps, uint256 maxBps);
    error ExceedsParent(uint256 sumChildrenPlusLoss, uint256 parentWeight);
    error CropMismatch();
    error EmptyLotList();
    error GradeAlreadyAttested(uint256 lotId);
    error MissingGradeAttestation(uint256 lotId);
    error LotAlreadySettled(uint256 lotId);
    error LineageConflictSettled(uint256 lotId, uint256 conflictingLotId);
    error NonceAlreadyUsed(address sender, uint256 nonce);
    error InvoiceAlreadyUsed(string invoiceId);
    error ClaimAlreadyExists(uint256 claimId);
    error ClaimNotFound(uint256 claimId);
    error InvalidAllocation(string reason);
    error ContractExpiredOrInactive();

    event LotRegistered(uint256 indexed lotId, address indexed owner, string cropId, uint256 weightG, string location, bytes32 newAuditHead);
    event LotTransferred(uint256 indexed lotId, address indexed from, address indexed to, uint256 receivedWeightG, uint256 lossG, uint8 reason, bytes32 newAuditHead);
    event LotSplit(uint256 indexed parentLotId, uint256[] childLotIds, uint256 lossG, bytes32 newAuditHead);
    event LotsMerged(uint256[] parentLotIds, uint256 indexed childLotId, uint256 totalWeightG, bytes32 newAuditHead);
    event GradeAttested(uint256 indexed attestationId, uint256 indexed lotId, uint8 grade, string evidenceCid, bytes32 newAuditHead);
    event ContractCreated(uint256 indexed contractId, address indexed processor, string cropId, uint256 qtyG, bytes32 newAuditHead);
    event AllocationCommitted(uint256 indexed contractId, uint256[] lotIds, uint256[] weightsG, string solverRunCid, bytes32 newAuditHead);
    event ClaimSubmitted(uint256 indexed claimId, uint256 indexed lotId, string invoiceId, uint256 amountPaise, address claimant, bytes32 newAuditHead);
    event ClaimSettled(uint256 indexed claimId, uint256 indexed lotId, uint256 amountPaise, bytes32 newAuditHead);
    event DisputeResolved(uint256 indexed lotId, uint256[] rejectedClaimIds, string solverRunCid, bytes32 newAuditHead);

    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        auditHead = keccak256(abi.encodePacked("AGROTRACE_GENESIS", block.chainid, address(this)));
    }

    function _updateAuditHead(bytes32 payloadHash) internal returns (bytes32) {
        auditHead = keccak256(abi.encodePacked(auditHead, payloadHash));
        return auditHead;
    }

    function _maxToleranceBps(uint8 reason) internal pure returns (uint256) {
        if (reason == LOSS_MOISTURE) return TOLERANCE_MOISTURE_BPS;
        if (reason == LOSS_TRANSPORT) return TOLERANCE_TRANSPORT_BPS;
        if (reason == LOSS_STORAGE) return TOLERANCE_STORAGE_BPS;
        if (reason == LOSS_SPILLAGE) return TOLERANCE_SPILLAGE_BPS;
        return 0;
    }

    function _checkLineageSettled(uint256 lotId) internal view {
        if (lotSettled[lotId]) revert LotAlreadySettled(lotId);

        uint256[] memory queue = new uint256[](100);
        uint256 front = 0;
        uint256 back = 0;
        queue[back++] = lotId;

        while (front < back) {
            uint256 current = queue[front++];
            uint256[] storage parents = lots[current].parentIds;
            for (uint256 i = 0; i < parents.length; i++) {
                uint256 pId = parents[i];
                if (lotSettled[pId]) revert LineageConflictSettled(lotId, pId);
                if (back < 100) queue[back++] = pId;
            }
        }

        back = 0;
        front = 0;
        queue[back++] = lotId;
        while (front < back) {
            uint256 current = queue[front++];
            uint256[] storage children = _childLotIds[current];
            for (uint256 i = 0; i < children.length; i++) {
                uint256 cId = children[i];
                if (lotSettled[cId]) revert LineageConflictSettled(lotId, cId);
                if (back < 100) queue[back++] = cId;
            }
        }
    }

    function registerLot(string calldata cropId, uint256 weightG, string calldata location) external returns (uint256) {
        if (!hasRole(FARMER_ROLE, msg.sender) && !hasRole(DEFAULT_ADMIN_ROLE, msg.sender)) {
            revert UnauthorizedRole(FARMER_ROLE, msg.sender);
        }

        lotCounter++;
        uint256 newId = lotCounter;
        Lot storage l = lots[newId];
        l.id = newId;
        l.owner = msg.sender;
        l.cropId = cropId;
        l.weightG = weightG;
        l.status = LotStatus.CREATED;

        bytes32 head = _updateAuditHead(keccak256(abi.encode(newId, msg.sender, cropId, weightG, location)));
        emit LotRegistered(newId, msg.sender, cropId, weightG, location, head);
        return newId;
    }

    function transferLot(uint256 id, address to, uint256 receivedWeightG, uint256 lossG, uint8 reason) external {
        Lot storage l = lots[id];
        if (l.id == 0) revert LotNotFound(id);
        if (l.owner != msg.sender) revert NotLotOwner(id, msg.sender);

        if (receivedWeightG + lossG != l.weightG) {
            revert ExceedsParent(receivedWeightG + lossG, l.weightG);
        }

        if (lossG > 0) {
            uint256 lossBps = (lossG * 10000) / l.weightG;
            uint256 maxBps = _maxToleranceBps(reason);
            if (lossBps > maxBps) revert LossAboveTolerance(lossBps, maxBps);
        }

        l.owner = to;
        l.weightG = receivedWeightG;
        l.lossG += lossG;
        l.lossReason = reason;
        l.status = LotStatus.RECEIVED;

        bytes32 head = _updateAuditHead(keccak256(abi.encode(id, msg.sender, to, receivedWeightG, lossG, reason)));
        emit LotTransferred(id, msg.sender, to, receivedWeightG, lossG, reason, head);
    }

    function splitLot(uint256 id, uint256[] calldata childWeightsG, uint256 lossG, uint8 reason) external returns (uint256[] memory) {
        Lot storage parent = lots[id];
        if (parent.id == 0) revert LotNotFound(id);
        if (parent.owner != msg.sender) revert NotLotOwner(id, msg.sender);

        uint256 sumChildren = 0;
        for (uint256 i = 0; i < childWeightsG.length; i++) {
            sumChildren += childWeightsG[i];
        }

        if (sumChildren + lossG != parent.weightG) {
            revert ExceedsParent(sumChildren + lossG, parent.weightG);
        }

        if (lossG > 0) {
            uint256 lossBps = (lossG * 10000) / parent.weightG;
            uint256 maxBps = _maxToleranceBps(reason);
            if (lossBps > maxBps) revert LossAboveTolerance(lossBps, maxBps);
        }

        uint256[] memory createdIds = new uint256[](childWeightsG.length);
        for (uint256 i = 0; i < childWeightsG.length; i++) {
            lotCounter++;
            uint256 childId = lotCounter;
            createdIds[i] = childId;

            Lot storage child = lots[childId];
            child.id = childId;
            child.parentIds.push(id);
            child.owner = msg.sender;
            child.cropId = parent.cropId;
            child.weightG = childWeightsG[i];
            child.gradeAttId = parent.gradeAttId;
            child.status = parent.gradeAttId != 0 ? LotStatus.GRADED : LotStatus.CREATED;

            _childLotIds[id].push(childId);
        }

        parent.weightG = 0;
        parent.status = LotStatus.ALLOCATED;

        bytes32 head = _updateAuditHead(keccak256(abi.encode(id, createdIds, lossG, reason)));
        emit LotSplit(id, createdIds, lossG, head);
        return createdIds;
    }

    function mergeLots(uint256[] calldata ids) external returns (uint256) {
        if (ids.length == 0) revert EmptyLotList();

        string memory crop = lots[ids[0]].cropId;
        uint256 totalWeight = 0;

        for (uint256 i = 0; i < ids.length; i++) {
            Lot storage l = lots[ids[i]];
            if (l.id == 0) revert LotNotFound(ids[i]);
            if (l.owner != msg.sender) revert NotLotOwner(ids[i], msg.sender);
            if (keccak256(bytes(l.cropId)) != keccak256(bytes(crop))) revert CropMismatch();

            totalWeight += l.weightG;
            l.weightG = 0;
            l.status = LotStatus.ALLOCATED;
        }

        lotCounter++;
        uint256 mergedId = lotCounter;
        Lot storage merged = lots[mergedId];
        merged.id = mergedId;
        merged.owner = msg.sender;
        merged.cropId = crop;
        merged.weightG = totalWeight;
        merged.status = LotStatus.RECEIVED;

        for (uint256 i = 0; i < ids.length; i++) {
            merged.parentIds.push(ids[i]);
            _childLotIds[ids[i]].push(mergedId);
        }

        bytes32 head = _updateAuditHead(keccak256(abi.encode(mergedId, ids, totalWeight)));
        emit LotsMerged(ids, mergedId, totalWeight, head);
        return mergedId;
    }

    function attestGrade(
        uint256 lotId,
        uint8 grade,
        uint256 moistureBps,
        uint256 impurityBps,
        string calldata evidenceCid,
        bytes32 evidenceSha256
    ) external returns (uint256) {
        if (!hasRole(GRADER_ROLE, msg.sender) && !hasRole(DEFAULT_ADMIN_ROLE, msg.sender)) {
            revert UnauthorizedRole(GRADER_ROLE, msg.sender);
        }

        Lot storage l = lots[lotId];
        if (l.id == 0) revert LotNotFound(lotId);
        if (l.gradeAttId != 0) revert GradeAlreadyAttested(lotId);

        gradeCounter++;
        uint256 attId = gradeCounter;

        gradeAttestations[attId] = GradeAttestation({
            id: attId,
            lotId: lotId,
            grade: grade,
            moistureBps: moistureBps,
            impurityBps: impurityBps,
            evidenceCid: evidenceCid,
            evidenceSha256: evidenceSha256,
            grader: msg.sender,
            timestamp: block.timestamp
        });

        l.gradeAttId = attId;
        l.status = LotStatus.GRADED;

        bytes32 head = _updateAuditHead(keccak256(abi.encode(attId, lotId, grade, evidenceCid, evidenceSha256)));
        emit GradeAttested(attId, lotId, grade, evidenceCid, head);
        return attId;
    }

    function createContract(
        string calldata cropId,
        uint256 qtyG,
        uint8 minGrade,
        uint256 basePricePerKgPaise,
        uint256[3] calldata gradeMultiplierBps,
        uint256 deadline,
        uint256 shortfallPenaltyPaise
    ) external returns (uint256) {
        if (!hasRole(PROCESSOR_ROLE, msg.sender) && !hasRole(DEFAULT_ADMIN_ROLE, msg.sender)) {
            revert UnauthorizedRole(PROCESSOR_ROLE, msg.sender);
        }

        contractCounter++;
        uint256 cId = contractCounter;

        contracts[cId] = ProcurementContract({
            id: cId,
            processor: msg.sender,
            cropId: cropId,
            qtyG: qtyG,
            minGrade: minGrade,
            basePricePerKgPaise: basePricePerKgPaise,
            gradeMultiplierBps: gradeMultiplierBps,
            deadline: deadline,
            shortfallPenaltyPaise: shortfallPenaltyPaise,
            allocatedQtyG: 0,
            active: true
        });

        bytes32 head = _updateAuditHead(keccak256(abi.encode(cId, msg.sender, cropId, qtyG, minGrade)));
        emit ContractCreated(cId, msg.sender, cropId, qtyG, head);
        return cId;
    }

    function commitAllocation(
        uint256 contractId,
        uint256[] calldata lotIds,
        uint256[] calldata weightsG,
        string calldata solverRunCid,
        bytes32 solverRunSha256
    ) external {
        ProcurementContract storage c = contracts[contractId];
        if (!c.active || block.timestamp > c.deadline) revert ContractExpiredOrInactive();
        if (lotIds.length != weightsG.length) revert InvalidAllocation("Mismatched arrays");

        uint256 additionalAllocation = 0;

        for (uint256 i = 0; i < lotIds.length; i++) {
            uint256 lId = lotIds[i];
            Lot storage l = lots[lId];
            if (l.id == 0) revert LotNotFound(lId);
            if (l.gradeAttId == 0) revert MissingGradeAttestation(lId);
            if (lotSettled[lId]) revert LotAlreadySettled(lId);

            GradeAttestation storage att = gradeAttestations[l.gradeAttId];
            if (att.grade < c.minGrade) revert InvalidAllocation("Lot quality below contract minGrade");

            if (l.allocatedWeightG + weightsG[i] > l.weightG) {
                revert InvalidAllocation("Allocation exceeds available lot weight");
            }

            for (uint256 j = i + 1; j < lotIds.length; j++) {
                if (lotIds[j] == lId) revert InvalidAllocation("Duplicate lot in allocation payload");
            }

            l.allocatedWeightG += weightsG[i];
            if (l.allocatedWeightG == l.weightG) {
                l.status = LotStatus.ALLOCATED;
            }
            additionalAllocation += weightsG[i];
        }

        if (c.allocatedQtyG + additionalAllocation > c.qtyG) {
            revert InvalidAllocation("Allocation exceeds contract capacity");
        }
        c.allocatedQtyG += additionalAllocation;

        bytes32 head = _updateAuditHead(keccak256(abi.encode(contractId, lotIds, weightsG, solverRunCid, solverRunSha256)));
        emit AllocationCommitted(contractId, lotIds, weightsG, solverRunCid, head);
    }

    function submitClaim(
        uint256 claimId,
        uint256 lotId,
        string calldata invoiceId,
        uint256 amountPaise,
        uint256 nonce
    ) external {
        if (claims[claimId].claimId != 0) revert ClaimAlreadyExists(claimId);
        if (usedInvoices[invoiceId]) revert InvoiceAlreadyUsed(invoiceId);
        if (usedNonces[msg.sender][nonce]) revert NonceAlreadyUsed(msg.sender, nonce);

        Lot storage l = lots[lotId];
        if (l.id == 0) revert LotNotFound(lotId);
        if (l.gradeAttId == 0) revert MissingGradeAttestation(lotId);

        _checkLineageSettled(lotId);

        usedInvoices[invoiceId] = true;
        usedNonces[msg.sender][nonce] = true;

        claims[claimId] = Claim({
            claimId: claimId,
            lotId: lotId,
            invoiceId: invoiceId,
            amountPaise: amountPaise,
            claimant: msg.sender,
            settled: false,
            rejected: false
        });

        bytes32 head = _updateAuditHead(keccak256(abi.encode(claimId, lotId, invoiceId, amountPaise, nonce)));
        emit ClaimSubmitted(claimId, lotId, invoiceId, amountPaise, msg.sender, head);
    }

    function settle(uint256 claimId) external {
        Claim storage cl = claims[claimId];
        if (cl.claimId == 0) revert ClaimNotFound(claimId);
        if (cl.settled) revert LotAlreadySettled(cl.lotId);
        if (cl.rejected) revert InvalidAllocation("Claim was rejected in dispute resolution");

        Lot storage l = lots[cl.lotId];
        if (lotSettled[l.id]) revert LotAlreadySettled(l.id);
        _checkLineageSettled(l.id);

        cl.settled = true;
        lotSettled[l.id] = true;
        l.status = LotStatus.SETTLED;

        bytes32 head = _updateAuditHead(keccak256(abi.encode(claimId, cl.lotId, cl.amountPaise, "SETTLED")));
        emit ClaimSettled(claimId, cl.lotId, cl.amountPaise, head);
    }

    function resolveDispute(
        uint256 lotId,
        uint256[] calldata rejectedClaimIds,
        string calldata solverRunCid
    ) external {
        if (!hasRole(DEFAULT_ADMIN_ROLE, msg.sender) && !hasRole(AUDITOR_ROLE, msg.sender)) {
            revert UnauthorizedRole(AUDITOR_ROLE, msg.sender);
        }

        for (uint256 i = 0; i < rejectedClaimIds.length; i++) {
            Claim storage cl = claims[rejectedClaimIds[i]];
            if (cl.claimId != 0) {
                cl.rejected = true;
            }
        }

        lots[lotId].status = LotStatus.GRADED;

        bytes32 head = _updateAuditHead(keccak256(abi.encode(lotId, rejectedClaimIds, solverRunCid)));
        emit DisputeResolved(lotId, rejectedClaimIds, solverRunCid, head);
    }

    function getLineage(uint256 lotId) external view returns (uint256[] memory ancestors, uint256[] memory descendants) {
        ancestors = lots[lotId].parentIds;
        descendants = _childLotIds[lotId];
    }

    function getAuditHead() external view returns (bytes32) {
        return auditHead;
    }
}
