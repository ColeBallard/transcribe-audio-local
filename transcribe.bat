@echo off
cd /d "%~dp0"
call venv\Scripts\activate.bat
echo.
echo Running transcription...
python transcribe.py %*
pause
