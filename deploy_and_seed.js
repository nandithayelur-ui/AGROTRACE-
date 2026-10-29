const hre = require("hardhat");
const fs = require("fs");
const path = require("path");

async function main() {
  const signers = await hre.ethers.getSigners();
  const [
    admin,
    farmerRavi,
    farmerMeena,
    collectorSuresh,
    warehouseMandya,
    warehouseMysuru,
    graderKavitha,
    processorAnnapurna,
    processorKaveri,
    auditorFCI
  ] = signers;

  console.log("================================================================================");
  console.log("AGROTRACE AI - DEPLOYING & SEEDING DEMO DATA");
  console.log("================================================================================");
  console.log(`Deployer / Admin: ${admin.address}`);

  const AgroTraceFactory = await hre.ethers.getContractFactory("AgroTrace");
  const agroTrace = await AgroTraceFactory.deploy();
  await agroTrace.waitForDeployment();
  const contractAddress = await agroTrace.getAddress();
  console.log(`AgroTrace Contract Deployed at: ${contractAddress}`);

  // 1. Assign Roles to Demo Accounts 0-9
  const FARMER_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("FARMER_ROLE"));
  const COLLECTOR_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("COLLECTOR_ROLE"));
  const WAREHOUSE_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("WAREHOUSE_ROLE"));
  const GRADER_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("GRADER_ROLE"));
  const PROCESSOR_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("PROCESSOR_ROLE"));
  const AUDITOR_ROLE = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("AUDITOR_ROLE"));

  await agroTrace.grantRole(FARMER_ROLE, farmerRavi.address);
  await agroTrace.grantRole(FARMER_ROLE, farmerMeena.address);
  await agroTrace.grantRole(COLLECTOR_ROLE, collectorSuresh.address);
  await agroTrace.grantRole(WAREHOUSE_ROLE, warehouseMandya.address);
  await agroTrace.grantRole(WAREHOUSE_ROLE, warehouseMysuru.address);
  await agroTrace.grantRole(GRADER_ROLE, graderKavitha.address);
  await agroTrace.grantRole(PROCESSOR_ROLE, processorAnnapurna.address);
  await agroTrace.grantRole(PROCESSOR_ROLE, processorKaveri.address);
  await agroTrace.grantRole(AUDITOR_ROLE, auditorFCI.address);
  console.log("-> Roles successfully granted to Hardhat demo accounts 0-9.");

  // 2. Seed Realistic Lots & Dag Ancestry (Wheat - Sharbati & Lokwan)
  // Lot 1: Farmer Ravi registers 1,000 kg (1,000,000 g) of Wheat in Mandya
  await agroTrace.connect(farmerRavi).registerLot("WHEAT_SHARBATI", 1000000, "Mandya-Farm-01");

  // Transfer Lot 1 to Collector Suresh: 15 kg (15,000 g) moisture loss (150 bps <= 300 bps tolerance) -> 985 kg received
  await agroTrace.connect(farmerRavi).transferLot(1, collectorSuresh.address, 985000, 15000, 0);

  // Transfer to Mandya Warehouse: 5 kg transit loss (50 bps <= 100 bps tolerance) -> 980 kg received
  await agroTrace.connect(collectorSuresh).transferLot(1, warehouseMandya.address, 975100, 9900, 1);

  // Split Lot 1 into Lot 2 (600 kg) and Lot 3 (375.1 kg) at warehouse
  const splitTx = await agroTrace.connect(warehouseMandya).splitLot(1, [600000, 375100], 0, 0);
  await splitTx.wait();

  // Farmer Meena registers Lot 4: 800 kg Wheat
  await agroTrace.connect(farmerMeena).registerLot("WHEAT_SHARBATI", 800000, "Mysuru-Farm-04");
  await agroTrace.connect(farmerMeena).transferLot(4, warehouseMysuru.address, 800000, 0, 0);

  // Seed remaining wheat lots to reach ~25 total lot records
  for (let i = 5; i <= 24; i++) {
    const w = 500000 + ((i * 37000) % 500000); // 500kg - 1000kg
    const farmer = i % 2 === 0 ? farmerRavi : farmerMeena;
    await agroTrace.connect(farmer).registerLot("WHEAT_LOKWAN", w, `Farm-Sector-${i}`);
  }
  console.log("-> 24 Wheat lots registered with splits and DAG ancestry.");

  // 3. Attest Grades (Kavitha Grader)
  const dummyHash = hre.ethers.keccak256(hre.ethers.toUtf8Bytes("EVIDENCE_FILE_CONTENT_V1"));
  await agroTrace.connect(graderKavitha).attestGrade(2, 3, 1150, 80, "bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi", dummyHash); // Grade 3 (Premium)
  await agroTrace.connect(graderKavitha).attestGrade(3, 2, 1300, 120, "bafybeihdwdcefghj5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi", dummyHash); // Grade 2 (Standard)
  await agroTrace.connect(graderKavitha).attestGrade(4, 3, 1100, 50, "bafybeicdeffgt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi", dummyHash); // Grade 3
  console.log("-> Official quality grades attested for Lots 2, 3, and 4.");

  // 4. Create 5 Processor Contracts
  const now = Math.floor(Date.now() / 1000);
  const oneWeek = now + 7 * 86400;

  // Contract 1: Annapurna Mills wants 1,500 kg Wheat Sharbati, minGrade 2, 3200 paise/kg (Rs. 32/kg)
  await agroTrace.connect(processorAnnapurna).createContract(
    "WHEAT_SHARBATI",
    1500000,
    2,
    3200,
    [9000, 10000, 11500], // Multipliers for Grades 1, 2, 3 (90%, 100%, 115%)
    oneWeek,
    50000
  );

  // Contract 2: Kaveri Foods wants 1,000 kg Wheat Lokwan, minGrade 1, 2800 paise/kg
  await agroTrace.connect(processorKaveri).createContract(
    "WHEAT_LOKWAN",
    1000000,
    1,
    2800,
    [9500, 10000, 11000],
    oneWeek,
    30000
  );

  // Contracts 3, 4, 5
  await agroTrace.connect(processorAnnapurna).createContract("WHEAT_SHARBATI", 2000000, 3, 3500, [8000, 10000, 12000], oneWeek, 80000);
  await agroTrace.connect(processorKaveri).createContract("WHEAT_LOKWAN", 500000, 2, 3000, [9000, 10000, 11000], oneWeek, 25000);
  await agroTrace.connect(processorAnnapurna).createContract("WHEAT_SHARBATI", 800000, 2, 3100, [9000, 10000, 11200], oneWeek, 40000);
  console.log("-> 5 Processor procurement contracts created.");

  // 5. Seed Claims (Including Planted Duplicate / Conflicting Claims for MIS/MVC)
  // Valid claim for Lot 2
  await agroTrace.connect(warehouseMandya).submitClaim(101, 2, "INV-2026-001", 1920000, 1);
  // Duplicate claim for the same lot (Planted conflict)
  try {
    await agroTrace.connect(collectorSuresh).submitClaim(102, 2, "INV-2026-002", 1920000, 1);
  } catch (e) {
    // Expected on-chain conflict or recorded in dispute registry
  }
  console.log("-> Planted claim set initialized.");

  // 6. Update .env with Contract Address
  const envPath = path.join(__dirname, ".env");
  if (fs.existsSync(envPath)) {
    let envContent = fs.readFileSync(envPath, "utf-8");
    if (envContent.includes("CONTRACT_ADDRESS=")) {
      envContent = envContent.replace(/CONTRACT_ADDRESS=.*/g, `CONTRACT_ADDRESS=${contractAddress}`);
    } else {
      envContent += `\nCONTRACT_ADDRESS=${contractAddress}`;
    }
    fs.writeFileSync(envPath, envContent, "utf-8");
    console.log(`-> Updated .env with CONTRACT_ADDRESS=${contractAddress}`);
  }

  const finalAuditHead = await agroTrace.getAuditHead();
  console.log(`-> On-chain Genesis Audit Head: ${finalAuditHead}`);
  console.log("================================================================================");
  console.log("SEEDING COMPLETE: Ready for unit tests and off-chain service integration.");
  console.log("================================================================================");
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});