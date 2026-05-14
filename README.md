# Transcribe Audio Local

**Fast, private, offline audio transcription using Faster-Whisper** 100% local.

---

## Features

- **Fully offline** transcription with OpenAI Whisper models
- High-quality English transcription (supports other languages too)
- **Timestamps** for every segment
- **Word-level timestamps** (very precise)
- Clean plain text output + detailed version
- **Drag & Drop** support via `.bat` file
- Automatic virtual environment setup
- Works with MP3, WAV, M4A, MP4, OGG, etc.
- GPU acceleration (CUDA) if available

---

## Quick Start (Windows)

### 1. Clone or Download the Repository

```bash
git clone https://github.com/yourusername/local-audio-transcriber.git
cd local-audio-transcriber
```

Or just download the ZIP and extract it.

### 2. Run Setup (One Time Only)

Double-click **`setup-transcriber_venv.bat`**  
→ **Run as Administrator** (recommended)

This will:
- Create a clean Python virtual environment (`venv`)
- Install Faster-Whisper + PyTorch
- Create `transcribe.bat` for easy use

> **Note**: First run may take 1–3 minutes while downloading models and dependencies.

---

## Usage

### Easiest Way: Drag & Drop

1. Put your audio file anywhere.
2. Drag the audio file onto **`transcribe.bat`**
3. Wait for transcription to finish.

A `.txt` file with the same name will appear next to your audio.

### Command Line

```cmd
transcribe.bat podcast.mp3
transcribe.bat interview.m4a --model medium
transcribe.bat meeting.wav --model large-v3 --device cpu
```

### Available Options

| Option            | Description                                      | Default     |
|-------------------|--------------------------------------------------|-------------|
| `--model`         | tiny / base / small / medium / large / large-v3 | `small`     |
| `--device`        | auto / cpu / cuda                                | `auto`      |
| `--plain-only`    | Output only clean text (no timestamps)           | False       |

---

## Requirements

- **Windows 10 or 11**
- Python 3.10+ installed (with `python` in PATH)
- FFmpeg (automatically installed by `winget` during setup)
- At least 4 GB RAM (8 GB+ recommended)
- Optional: NVIDIA GPU for much faster transcription

---

## Troubleshooting

**"Python not found"**  
→ Make sure Python is installed and added to PATH during installation.

**Setup gets stuck**  
→ Delete the `venv` folder and run `setup-transcriber_venv.bat` again.

**Slow transcription**  
→ Use `--model small` or add `--device cpu` if GPU causes issues.

**No timestamps**  
→ Remove `--plain-only` flag.

---

## Contributing

Feel free to open issues or pull requests!  
Common improvements welcome:
- Support for macOS/Linux scripts
- Speaker diarization (WhisperX)
- GUI version
- Batch processing folder support

---