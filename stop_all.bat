@echo off
echo [INFO] Stopping AgroTrace AI services...

:: Kill by window title
taskkill /fi "WindowTitle eq Hardhat Node" /f >nul 2>&1
taskkill /fi "WindowTitle eq FastAPI" /f >nul 2>&1
taskkill /fi "WindowTitle eq Vite Frontend" /f >nul 2>&1

:: Also kill by port
for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":8545 " ^| findstr "LISTENING" 2^>nul') do taskkill /f /pid %%p >nul 2>&1
for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":8080 " ^| findstr "LISTENING" 2^>nul') do taskkill /f /pid %%p >nul 2>&1
for /f "tokens=5" %%p in ('netstat -aon ^| findstr ":5173 " ^| findstr "LISTENING" 2^>nul') do taskkill /f /pid %%p >nul 2>&1

echo [OK] All services stopped.
