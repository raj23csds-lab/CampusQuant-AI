# CampusQuant AI - PowerShell Enterprise Launcher
Write-Host "=========================================================================" -ForegroundColor Cyan
Write-Host "              CAMPUSQUANT AI - ENTERPRISE LAUNCHER (PS1)" -ForegroundColor Cyan
Write-Host "=========================================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/3] Cleaning up existing background Python & Node processes..." -ForegroundColor Yellow
Get-Process -Name python, node -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
Write-Host "[OK] Processes cleaned successfully!" -ForegroundColor Green
Write-Host ""

$projectDir = $PSScriptRoot
Set-Location $projectDir

Write-Host "[2/3] Verifying Runtimes..." -ForegroundColor Yellow
$pythonExe = Join-Path $projectDir ".venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    Write-Host "[ERROR] Virtual environment python.exe not found at $pythonExe" -ForegroundColor Red
    exit 1
}

Write-Host "[3/3] Launching FastAPI Backend & Vite Frontend Servers..." -ForegroundColor Yellow
Start-Process cmd.exe -ArgumentList "/k cd /d ""$projectDir"" && .venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000 --reload"
Start-Process cmd.exe -ArgumentList "/k cd /d ""$projectDir\frontend"" && npm run dev"

Write-Host ""
Write-Host "=========================================================================" -ForegroundColor Green
Write-Host "  [SUCCESS] All CampusQuant AI Services Started!" -ForegroundColor Green
Write-Host "  - Backend API:  http://127.0.0.1:8000" -ForegroundColor White
Write-Host "  - Frontend App: http://localhost:5173" -ForegroundColor White
Write-Host ""
Write-Host "  Opening web app in default browser..." -ForegroundColor Yellow
Write-Host "=========================================================================" -ForegroundColor Green

Start-Sleep -Seconds 4
Start-Process "http://localhost:5173"
