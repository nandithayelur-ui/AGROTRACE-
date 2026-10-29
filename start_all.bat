@echo off
setlocal EnableDelayedExpansion

echo ============================================================
echo  AgroTrace AI - One-Click Start (Autonomous Launcher)
echo ============================================================

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Install Python 3.10+ and add to PATH.
    exit /b 1
)

:: Check Node
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found. Install Node 20+ and add to PATH.
    exit /b 1
)

echo [OK] Python and Node found

:: Kill any existing processes on our ports
echo [INFO] Clearing ports 8545, 8080, 5173...
for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":8545 " ^| findstr "LISTENING" 2^>nul') do taskkill /f /pid %%p >nul 2>&1
for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":8080 " ^| findstr "LISTENING" 2^>nul') do taskkill /f /pid %%p >nul 2>&1
for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":5173 " ^| findstr "LISTENING" 2^>nul') do taskkill /f /pid %%p >nul 2>&1

:: Create logs dir if missing
if not exist logs mkdir logs

:: Check keys (warn only)
echo [INFO] Checking API keys...
.venv\Scripts\python.exe scripts\check_keys.py

:: Start Hardhat node
echo [INFO] Starting Hardhat node on port 8545...
start "Hardhat Node" cmd /c "npx.cmd hardhat node --port 8545 > logs\hardhat.log 2>&1"
timeout /t 4 /nobreak >nul

:: Deploy and seed
echo [INFO] Deploying contracts and seeding data...
cmd /c "npx.cmd hardhat run deploy_and_seed.js --network localhost > logs\deploy.log 2>&1"
if errorlevel 1 (
    echo [WARN] Deploy/seed had issues - check logs\deploy.log
) else (
    echo [OK] Contracts deployed and seeded
)

:: Sync events into SQLite
echo [INFO] Syncing events into cache...
.venv\Scripts\python.exe chain\indexer.py > logs\indexer.log 2>&1

:: Start FastAPI
echo [INFO] Starting FastAPI on port 8080...
start "FastAPI" cmd /c ".venv\Scripts\python.exe -m uvicorn api.main:app --host 127.0.0.1 --port 8080 > logs\api.log 2>&1"
timeout /t 3 /nobreak >nul

:: Wait for API health
echo [INFO] Waiting for API health check...
set attempts=0
:waitloop
set /a attempts+=1
if %attempts% gtr 20 (
    echo [WARN] API did not respond in time - check logs\api.log
    goto :startfrontend
)
curl -sf http://127.0.0.1:8080/health >nul 2>&1
if errorlevel 1 (
    timeout /t 2 /nobreak >nul
    goto :waitloop
)
echo [OK] API is healthy

:startfrontend
:: Start Vite frontend
echo [INFO] Starting Vite frontend on port 5173...
start "Vite Frontend" cmd /c "cd frontend && npm.cmd run dev > ..\logs\frontend.log 2>&1"
timeout /t 3 /nobreak >nul

:: Open browser
echo [INFO] Opening browser...
start "" http://localhost:5173

echo.
echo ============================================================
echo  AgroTrace AI is running!
echo   API:      http://127.0.0.1:8080
echo   Frontend: http://localhost:5173
echo   Health:   http://127.0.0.1:8080/health
echo   Logs:     logs\
echo ============================================================
echo  Run stop_all.bat to stop all services.
echo ============================================================
