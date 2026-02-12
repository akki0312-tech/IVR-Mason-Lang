# MASON IVR - Quick Start Script
# This script helps you set up the backend quickly

Write-Host "=== MASON IVR Backend Setup ===" -ForegroundColor Cyan
Write-Host ""

# Check Python version
Write-Host "Checking Python version..." -ForegroundColor Yellow
$pythonVersion = python --version 2>&1
if ($pythonVersion -match "Python 3\.([0-9]+)") {
    $minorVersion = [int]$matches[1]
    if ($minorVersion -ge 10) {
        Write-Host "✓ Python version OK: $pythonVersion" -ForegroundColor Green
    } else {
        Write-Host "✗ Python 3.10+ required. Found: $pythonVersion" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✗ Python not found or version check failed" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Create virtual environment
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

Write-Host ""

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

Write-Host ""

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "=== Setup Complete! ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Copy .env.example to .env and fill in your API keys"
Write-Host "2. Make sure you have your Google Cloud credentials JSON file"
Write-Host "3. Run: uvicorn app:app --reload"
Write-Host ""
