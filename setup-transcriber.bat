@echo off
setlocal enabledelayedexpansion

echo ========================================
echo     Local Audio Transcriber - VENV Setup
echo ========================================
echo.

:: Go to the script's folder
cd /d "%~dp0"

:: === 1. Check/Create Virtual Environment ===
echo [1/4] Checking virtual environment...
if not exist "venv\Scripts\activate.bat" (
    echo Creating new virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Python not found or venv creation failed.
        echo    Make sure Python is installed and added to PATH.
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created.
) else (
    echo ✅ Virtual environment already exists.
)

:: === 2. Activate venv and install dependencies ===
echo.
echo [2/4] Activating venv and installing packages...
call venv\Scripts\activate.bat

:: Upgrade pip
python -m pip install --upgrade pip

:: Install faster-whisper + torch (with CUDA if possible)
echo Installing faster-whisper...
python -m pip install faster-whisper

:: Torch with CUDA support (cu121 is widely compatible in 2026)
echo Installing PyTorch...
python -m pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121

echo.
echo [3/4] Installation finished!
echo.

:: === 3. Create a convenient run script ===
echo [4/4] Creating "transcribe.bat" for easy use...
(
echo @echo off
echo cd /d "%%~dp0"
echo call venv\Scripts\activate.bat
echo echo.
echo echo Running transcription...
echo python transcribe.py %%*
echo pause
) > transcribe.bat

echo.
echo ========================================
echo ✅ SETUP COMPLETE!
echo ========================================
echo.
echo You can now double-click **transcribe.bat** and drag-and-drop audio files onto it,
echo or run it from command line like this:
echo.
echo    transcribe.bat your_audio.mp3
echo    transcribe.bat meeting.m4a --model medium
echo.
echo (You only need to run this setup once)
echo.

pause