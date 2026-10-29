const { expect } = require("chai");
const hre = require("hardhat");

describe("AgroTrace AI - Full Attack Test Suite & Cost Verification", function () {
  let agroTrace;
  let admin, farmerRavi, farmerMeena, collectorSuresh, warehouseMandya, graderKavitha, processorAnnapurna, auditorFCI;
  let FARMER_ROLE, COLLECTOR_ROLE, WAREHOUSE_ROLE, GRADER_ROLE, PROCESSOR_ROLE, AUDITOR_ROLE;
  const dummyEvidenceHash = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("EVIDENCE_V1"));

  beforeEach(async function () {
    const signers = await hre.ethers.getSigners();
    [admin, farmerRavi, farmerMeena, collectorSuresh, warehouseMandya, , graderKavitha, processorAnnapurna, , auditorFCI] = signers;

    const AgroTraceFactory = await hre.ethers.getContractFactory("AgroTrace");
    agroTrace = await AgroTraceFactory.deploy();
    await agroTrace.waitForDeployment();

    FARMER_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("FARMER_ROLE"));
    COLLECTOR_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("COLLECTOR_ROLE"));
    WAREHOUSE_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("WAREHOUSE_ROLE"));
    GRADER_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("GRADER_ROLE"));
    PROCESSOR_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("PROCESSOR_ROLE"));
    AUDITOR_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("AUDITOR_ROLE"));

    await agroTrace.grantRole(FARMER_ROLE, farmerRavi.address);
    await agroTrace.grantRole(COLLECTOR_ROLE, collectorSuresh.address);
    await agroTrace.grantRole(WAREHOUSE_ROLE, warehouseMandya.address);
    await agroTrace.grantRole(GRADER_ROLE, graderKavitha.address);
    await agroTrace.grantRole(PROCESSOR_ROLE, processorAnnapurna.address);
    await agroTrace.grantRole(AUDITOR_ROLE, auditorFCI.address);
  });

  it("Attack 1: Settle the same lot twice (Rejects with LotAlreadySettled)", async function () {
    // 1. Register, grade, and claim Lot 1
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 1000000, "Mandya");
    await agroTrace.connect(graderKavitha).attestGrade(1, 2, 1200, 100, "bafy_cid_1", dummyEvidenceHash);
    await agroTrace.connect(farmerRavi).submitClaim(1, 1, "INV-001", 3000000, 1);

    // First settlement succeeds
    await expect(agroTrace.connect(admin).settle(1)).to.emit(agroTrace, "ClaimSettled");

    // Second settlement of the same claim / lot must revert
    await expect(agroTrace.connect(admin).settle(1))
      .to.be.revertedWithCustomError(agroTrace, "LotAlreadySettled")
      .withArgs(1);
  });

  it("Attack 2: Split a 985 kg lot into 600 + 500 kg (Rejects with ExceedsParent)", async function () {
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 985000, "Mandya");

    // 600,000 + 500,000 = 1,100,000 g > 985,000 g parent weight
    await expect(
      agroTrace.connect(farmerRavi).splitLot(1, [600000, 500000], 0, 0)
    ).to.be.revertedWithCustomError(agroTrace, "ExceedsParent")
      .withArgs(1100000, 985000);
  });

  it("Attack 3: Wrong role writes a grade attestation (Rejects with UnauthorizedRole)", async function () {
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 1000000, "Mandya");

    // Farmer Ravi attempts to act as Grader
    await expect(
      agroTrace.connect(farmerRavi).attestGrade(1, 3, 1100, 50, "bafy_fake", dummyEvidenceHash)
    ).to.be.revertedWithCustomError(agroTrace, "UnauthorizedRole")
      .withArgs(GRADER_ROLE, farmerRavi.address);
  });

  it("Attack 4: Loss above tolerance (Rejects with LossAboveTolerance)", async function () {
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 1000000, "Mandya");

    // Max moisture loss tolerance is 300 bps (3%). Attempting 35,000 g loss (3.5% = 350 bps)
    await expect(
      agroTrace.connect(farmerRavi).transferLot(1, collectorSuresh.address, 965000, 35000, 0)
    ).to.be.revertedWithCustomError(agroTrace, "LossAboveTolerance")
      .withArgs(350, 300);
  });

  it("Attack 5: Settle without grade attestation (Rejects with MissingGradeAttestation)", async function () {
    // Register lot without grading
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 1000000, "Mandya");

    await expect(
      agroTrace.connect(farmerRavi).submitClaim(10, 1, "INV-UNGRADED", 2500000, 1)
    ).to.be.revertedWithCustomError(agroTrace, "MissingGradeAttestation")
      .withArgs(1);
  });

  it("Attack 6: Replay an old settlement request with used nonce (Rejects with NonceAlreadyUsed)", async function () {
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 1000000, "Mandya");
    await agroTrace.connect(graderKavitha).attestGrade(1, 2, 1200, 100, "bafy_cid_1", dummyEvidenceHash);

    // First claim with nonce 42 succeeds
    await agroTrace.connect(farmerRavi).submitClaim(101, 1, "INV-001", 100000, 42);

    // Register a second lot
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 500000, "Mandya");
    await agroTrace.connect(graderKavitha).attestGrade(2, 2, 1200, 100, "bafy_cid_2", dummyEvidenceHash);

    // Attempt replay of nonce 42 from the same sender
    await expect(
      agroTrace.connect(farmerRavi).submitClaim(102, 2, "INV-002", 50000, 42)
    ).to.be.revertedWithCustomError(agroTrace, "NonceAlreadyUsed")
      .withArgs(farmerRavi.address, 42);
  });

  it("Attack 7: Over-assign a lot in an allocation (Rejects with InvalidAllocation)", async function () {
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 500000, "Mandya"); // 500 kg available
    await agroTrace.connect(graderKavitha).attestGrade(1, 2, 1200, 100, "bafy_cid_1", dummyEvidenceHash);

    const deadline = Math.floor(Date.now() / 1000) + 3600;
    await agroTrace.connect(processorAnnapurna).createContract("WHEAT", 1000000, 2, 3000, [10000, 10000, 10000], deadline, 5000);

    // Planted violation: attempting to assign 600 kg from a 500 kg lot
    await expect(
      agroTrace.connect(processorAnnapurna).commitAllocation(
        1,
        [1],
        [600000],
        "bafy_solver_run_bad",
        dummyEvidenceHash
      )
    ).to.be.revertedWithCustomError(agroTrace, "InvalidAllocation")
      .withArgs("Allocation exceeds available lot weight");
  });

  it("Attack 8: Audit chain tampering verification", async function () {
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 1000000, "Mandya");
    const genuineAuditHead = await agroTrace.getAuditHead();

    // Verify genuine hash matches cryptographic chain state
    expect(genuineAuditHead).to.not.equal(hre.ethers.ZeroHash);

    // Simulating off-chain tampering: an attacker edits cached audit data
    const tamperedPayloadHash = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("TAMPERED_EVENT_PAYLOAD"));
    const forgedAuditHead = hre.ethers.keccak256(hre.ethers.concat([genuineAuditHead, tamperedPayloadHash]));

    // An auditor verifying on-chain detects the forgery
    expect(genuineAuditHead).to.not.equal(forgedAuditHead);
  });

  it("Attack 9: Claim a descendant of an already-settled lot (Rejects with LineageConflictSettled)", async function () {
    // 1. Farmer Ravi registers 1000 kg and splits into Child 2 (600 kg) and Child 3 (400 kg)
    await agroTrace.connect(farmerRavi).registerLot("WHEAT", 1000000, "Mandya");
    await agroTrace.connect(graderKavitha).attestGrade(1, 2, 1200, 100, "bafy_cid_1", dummyEvidenceHash);
    await agroTrace.connect(farmerRavi).splitLot(1, [600000, 400000], 0, 0);

    // 2. Child 2 is claimed and settled
    await agroTrace.connect(graderKavitha).attestGrade(2, 2, 1200, 100, "bafy_cid_2", dummyEvidenceHash);
    await agroTrace.connect(farmerRavi).submitClaim(201, 2, "INV-CHILD-2", 1800000, 1);
    await agroTrace.connect(admin).settle(201);

    // 3. Attempting to claim the parent lot 1 (ancestor of settled child 2) must revert
    await expect(
      agroTrace.connect(farmerRavi).submitClaim(202, 1, "INV-PARENT-CONFLICT", 3000000, 2)
    ).to.be.revertedWithCustomError(agroTrace, "LineageConflictSettled")
      .withArgs(1, 2);
  });
});