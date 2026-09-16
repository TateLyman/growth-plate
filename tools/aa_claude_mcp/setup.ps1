$ErrorActionPreference = "Stop"

if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
  Write-Error "Python launcher 'py' not found. Install Python 3.10+ first."
}

Set-Location $PSScriptRoot

py -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt

$venvPy = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$server = Join-Path $PSScriptRoot "aa_mcp.py"
$fixture = Join-Path $PSScriptRoot "dev\stub_aa_app.py"
$smoke = Join-Path $PSScriptRoot "dev\smoke_test.py"

Write-Host ""
Write-Host "MCP bridge installed."
Write-Host ""
Write-Host "Start a local endpoint first - either a real local Anna's Archive instance"
Write-Host "(http://localtest.me:8000), or the bundled dev fixture:"
Write-Host "  & `"$venvPy`" `"$fixture`" --port 8000"
Write-Host ""
Write-Host "Verify the bridge end to end:"
Write-Host "  & `"$venvPy`" `"$smoke`""
Write-Host ""
Write-Host "Register with Claude Code:"
Write-Host "  claude mcp add --transport stdio --scope user annas-local -- `"$venvPy`" `"$server`""
Write-Host ""
Write-Host "Verify:"
Write-Host "  claude mcp list"
Write-Host "  then inside Claude Code: /mcp"
