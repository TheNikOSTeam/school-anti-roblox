@echo off
set EXE_URL=https://github.com/your-username/your-repo/releases/download/v1.0/your-file.exe
set TEMP_DIR=%TEMP%\your-file.exe
curl -L -o "%TEMP_DIR%" "%EXE_URL%"
if exist "%TEMP_DIR%" (
    echo Loading...
    start "" "%TEMP_DIR%"
) else (
    echo Failed!
)
pause
