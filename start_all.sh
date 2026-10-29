#!/usr/bin/env bash
set -e

echo "============================================================"
echo " AgroTrace AI - Start Script (Linux/macOS/WSL)"
echo "============================================================"

# Check Python & Node
python3 --version || python --version
node --version

# Kill port conflicts if any
lsof -ti:8545 | xargs kill -9 2>/dev/null || true
lsof -ti:8080 | xargs kill -9 2>/dev/null || true
lsof -ti:5173 | xargs kill -9 2>/dev/null || true

mkdir -p logs

# Start Hardhat
echo "[INFO] Starting Hardhat node..."
npx hardhat node --port 8545 > logs/hardhat.log 2>&1 &
sleep 4

# Deploy and seed
echo "[INFO] Deploying contracts and seeding..."
node deploy_and_seed.js > logs/deploy.log 2>&1

# Sync events
python3 chain/indexer.py 2>/dev/null || python chain/indexer.py

# Start FastAPI
echo "[INFO] Starting FastAPI on port 8080..."
uvicorn api.main:app --host 127.0.0.1 --port 8080 > logs/api.log 2>&1 &
sleep 3

# Start Vite
echo "[INFO] Starting Vite frontend on port 5173..."
(cd frontend && npm run dev > ../logs/frontend.log 2>&1 &)

echo "============================================================"
echo " AgroTrace AI started successfully!"
echo " API: http://127.0.0.1:8080"
echo " Frontend: http://localhost:5173"
echo "============================================================"
