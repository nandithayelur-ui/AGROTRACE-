Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "AGROTRACE AI - FULL REPRODUCTION PIPELINE (WINDOWS POWERSHELL)" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan

# 1. Compile contracts
Write-Host "`n1. Compiling Smart Contracts..." -ForegroundColor Yellow
npx hardhat compile

# 2. Run Hardhat Security Attack Tests
Write-Host "`n2. Running Hardhat Attack Tests..." -ForegroundColor Yellow
$env:REPORT_GAS="true"; npx hardhat test

# 3. Deploy & Seed
Write-Host "`n3. Deploying and Seeding Demo Lots..." -ForegroundColor Yellow
npx hardhat run scripts/deploy_and_seed.js --network localhost

# 4. Sync Indexer Cache
Write-Host "`n4. Syncing On-Chain Events to SQLite Cache..." -ForegroundColor Yellow
py -m chain.indexer

# 5. Run All Pytest Suites
Write-Host "`n5. Running Complete Pytest Suite..." -ForegroundColor Yellow
py -m pytest tests/ -v

# 6. Run Benchmark
Write-Host "`n6. Running Optimization Benchmark..." -ForegroundColor Yellow
py scripts/benchmark.py

Write-Host "`nReproduction pipeline completed successfully." -ForegroundColor Green
