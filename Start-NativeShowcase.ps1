[CmdletBinding()]
param(
    [ValidateRange(1, 65535)][int]$Port = 8814,
    [switch]$Rebuild,
    [switch]$Windowed,
    [switch]$NoBackendStart,
    [ValidateSet('overview', 'live', 'demos', 'hybrid', 'industries', 'showoff', 'build', 'sizing', 'platforms', 'deviceclasses', 'business', 'playbook', 'learn')][string]$Section,
    [switch]$Wait
)
# Launches the native WinUI 3 Surface Hybrid Intelligence x Retail (never a browser).
# Backend lifecycle is owned by the app: it reuses a showcase service already on
# 127.0.0.1:$Port (left running on exit), otherwise it starts server.py with
# HYBRID_RETAIL_PYTHON, the project .venv or the sibling Foundry SDK venv, logs to
# .runtime\native\backend-*.log and stops
# only that owned child when the window closes (a Windows job object also
# prevents an orphan if the app crashes).

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$project = Join-Path $root 'native\HybridIntelligenceRetail.csproj'
$candidates = @(
    (Join-Path $root 'native\bin\Release\net10.0-windows10.0.26100.0\win-arm64\HybridIntelligenceRetail.exe'),
    (Join-Path $root 'native\bin\ARM64\Release\net10.0-windows10.0.26100.0\win-arm64\HybridIntelligenceRetail.exe')
)

function Find-Exe { $candidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1 }

function Find-Dotnet {
    $known = @(
        $env:HYBRID_RETAIL_DOTNET,
        (Join-Path (Split-Path $root -Parent) 'asu-agentic-showcase\.tools\dotnet\dotnet.exe')
    ) | Where-Object { $_ -and (Test-Path -LiteralPath $_) }
    if ($known) { return @($known)[0] }
    $onPath = Get-Command dotnet.exe -ErrorAction SilentlyContinue
    if ($onPath) { return $onPath.Source }
    $installed = @((Join-Path $env:ProgramFiles 'dotnet\dotnet.exe'), (Join-Path $env:USERPROFILE '.dotnet\dotnet.exe')) |
        Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
    if ($installed) { return $installed }
    throw 'No .NET SDK found. Install the .NET 10 SDK or set HYBRID_RETAIL_DOTNET to dotnet.exe.'
}

$exe = Find-Exe
if ($Rebuild -or -not $exe) {
    $dotnet = Find-Dotnet
    Write-Host "Building Surface Hybrid Intelligence x Retail with $dotnet ..."
    & $dotnet build $project -c Release -nologo -v minimal
    if ($LASTEXITCODE -ne 0) { throw "Native build failed (exit $LASTEXITCODE)." }
    $exe = Find-Exe
    if (-not $exe) { throw 'Build completed but HybridIntelligenceRetail.exe was not found.' }
}

$arguments = @('--port', $Port, '--root', "`"$root`"")
if ($Windowed) { $arguments += '--windowed' }
if ($NoBackendStart) { $arguments += '--no-backend-start' }
if ($Section) { $arguments += @('--section', $Section) }

Write-Host "Launching $exe"
$process = Start-Process -FilePath $exe -ArgumentList $arguments -WorkingDirectory (Split-Path $exe) -PassThru
if ($Wait) {
    $process.WaitForExit()
    exit $process.ExitCode
}
