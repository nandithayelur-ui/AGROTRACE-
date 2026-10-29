#!/usr/bin/env bash
set -e
echo "================================================================================"
echo "AGROTRACE AI - FULL REPRODUCTION PIPELINE (BASH)"
echo "================================================================================"

echo -e "\n1. Compiling Smart Contracts..."
npx hardhat compile

echo -e "\n2. Running Hardhat Attack Tests..."
REPORT_GAS=true npx hardhat test

echo -e "\n3. Deploying and Seeding Demo Lots..."
npx hardhat run scripts/deploy_and_seed.js --network localhost

echo -e "\n4. Syncing On-Chain Events to SQLite Cache..."
python3 -m chain.indexer

echo -e "\n5. Running Complete Pytest Suite..."
pytest tests/ -v

echo -e "\n6. Running Optimization Benchmark..."
python3 scripts/benchmark.py

echo -e "\nReproduction pipeline completed successfully."
