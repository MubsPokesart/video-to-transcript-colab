# video-to-transcript-colab

> Transform your videos and audio files into accurate text transcripts using OpenAI's Whisper AI — powered by Google Colab or run locally.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991.svg)](https://github.com/openai/whisper)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

---

## Overview

**Video-to-Transcript** is a simple, powerful tool that automatically transcribes video and audio files using OpenAI's state-of-the-art Whisper speech recognition model. Whether you're processing lectures, podcasts, interviews, or personal recordings, this tool makes it easy to extract text transcripts in minutes.

**Why this project?**
- **Zero-setup option**: Run directly in Google Colab with free GPU access
- **Local flexibility**: Process files on your own machine with full control
- **Batch processing**: Transcribe entire folders automatically
- **Smart skipping**: Avoids re-processing files that already have transcripts
- **Multi-format support**: Works with MP4, MOV, MP3, WAV, FLAC, and more

---

## 📑 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
  - [Option 1: Google Colab (Recommended for Beginners)](#option-1-google-colab-recommended-for-beginners)
  - [Option 2: Local Setup](#option-2-local-setup)
- [Usage](#-usage)
  - [Using Google Colab](#using-google-colab)
  - [Using Local Script](#using-local-script)
- [Configuration](#-configuration)
- [Supported Formats](#-supported-formats)
- [Model Selection Guide](#-model-selection-guide)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## Features

- **Powered by OpenAI Whisper**: Industry-leading speech recognition accuracy
- **Cloud & Local Options**: Run in Google Colab (free GPU) or on your local machine
- **Batch Processing**: Process entire directories of files automatically
- **Resume Capability**: Skips already-transcribed files to save time
- **Flexible Model Sizes**: Choose from tiny to large models based on your accuracy/speed needs
- **Clean Text Output**: Generates plain text transcripts ready for further use
- **Multi-language Support**: Whisper supports 99+ languages (use non-`.en` models)

---

## Installation

### Option 1: Google Colab (Recommended for Beginners)

No installation required! Simply:

1. Open the notebook: `colab/whisper_video_to_transcript.ipynb`
2. Click **"Open in Colab"** or upload to your Google Drive
3. Ensure GPU is enabled: `Runtime → Change runtime type → GPU (T4)`
4. Run the cells in order

**Requirements**: A Google account and files stored in Google Drive.

---

### Option 2: Local Setup

**Prerequisites**:
- Python 3.8 or higher
- FFmpeg (for audio processing)
- (Optional) CUDA-compatible GPU for faster processing

#### Step 1: Install FFmpeg

**macOS**:
```bash
brew install ffmpeg
```

**Ubuntu/Debian**:
```bash
sudo apt update && sudo apt install ffmpeg
```

**Windows**:
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

#### Step 2: Clone the Repository

```bash
git clone https://github.com/yourusername/video-to-transcript-colab.git
cd video-to-transcript-colab/local
```

#### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs OpenAI Whisper and its dependencies.

---

## Usage

### Using Google Colab

1. **Upload your video/audio files** to Google Drive
2. **Open the notebook**: `colab/whisper_video_to_transcript.ipynb`
3. **Update the configuration** (Cell 3):
   ```python
   SOURCE_DIR = "/content/drive/MyDrive/YOUR_FOLDER_NAME"
   MODEL_NAME = "small.en"  # Adjust model size as needed
   ```
4. **Run all cells** (`Runtime → Run all`)
5. **Find your transcripts** in: `/content/drive/MyDrive/whisper_transcripts/`

**Example Output**:
```
Transcripts will be saved to: /content/drive/MyDrive/whisper_transcripts
Loading Whisper model 'small.en'...
Model loaded successfully.

--- Transcribing 'lecture01.mp4'... ---
--- Finished 'lecture01.mp4'. Saved to 'whisper_transcripts/lecture01.txt' ---
Time taken: 45.32 seconds
```

---

### Using Local Script

1. **Place your files** in the `local/videos/` directory:
   ```
   local/
   ├── videos/          # ← Put your files here
   ├── transcripts/     # ← Transcripts appear here
   └── main.py
   ```

2. **Run the script**:
   ```bash
   python main.py
   ```

3. **Transcripts** will be saved in `local/transcripts/` with the same filename (`.txt` extension).

**Example**:
```bash
$ python main.py
Transcripts will be saved to: /path/to/local/transcripts
Loading Whisper model 'base'...
Model loaded successfully.
--- Transcribing 'interview.mp3'... ---
--- Finished 'interview.mp3'. Saved to 'transcripts/interview.txt' ---
```

---

## ⚙️ Configuration

### Key Settings (Colab & Local)

| Parameter | Description | Options |
|-----------|-------------|---------|
| `SOURCE_DIR` | Folder containing your video/audio files | Any valid path |
| `TRANSCRIPT_DIR` / `OUTPUT_DIR` | Where transcripts are saved | Any valid path |
| `MODEL_NAME` | Whisper model to use | `tiny`, `base`, `small`, `medium`, `large`, `large-v2` (add `.en` for English-only) |
| `SUPPORTED_EXTENSIONS` | File types to process | `.mp4`, `.mov`, `.m4a`, `.mp3`, `.wav`, `.flac` |

**Colab Configuration** (Cell 3):
```python
SOURCE_DIR = "/content/drive/MyDrive/Podcasts"
TRANSCRIPT_DIR = "/content/drive/MyDrive/whisper_transcripts"
MODEL_NAME = "medium"  # Higher accuracy, slower
```

**Local Configuration** (`main.py`, lines 8-10):
```python
SOURCE_DIR = os.path.join(dirname, "videos")
OUTPUT_DIR = os.path.join(dirname, "transcripts")
model = load_whisper_model("small")  # Change model size here
```

---

## 🎬 Supported Formats

The tool supports the following audio and video formats:

- **Video**: `.mp4`, `.mov`
- **Audio**: `.mp3`, `.m4a`, `.wav`, `.flac`

Whisper automatically extracts audio from video files.

---

## 🧠 Model Selection Guide

| Model | Size | Speed | Accuracy | Best For |
|-------|------|-------|----------|----------|
| `tiny` | 39 MB | Fastest | Lower | Quick drafts, testing |
| `base` | 74 MB | Fast | Good | General use, short clips |
| `small` | 244 MB | Moderate | Better | Most use cases |
| `medium` | 769 MB | Slow | High | Longer content, accuracy matters |
| `large` / `large-v2` | 1550 MB | Slowest | Highest | Professional transcription |

**English-only models** (e.g., `small.en`): Faster and more accurate for English audio. Use non-`.en` models for multilingual content.

**Recommendation**: Start with `small` or `small.en` for a good balance of speed and accuracy.

---

## 🛠️ Troubleshooting

### "Error loading model" in Colab
- **Solution**: Ensure GPU is enabled (`Runtime → Change runtime type → GPU`)

### "ModuleNotFoundError: No module named 'whisper'"
- **Solution**: Run `pip install git+https://github.com/openai/whisper.git`

### "ffmpeg not found"
- **Solution**: Install FFmpeg (see [Installation](#option-2-local-setup))

### Slow transcription on local machine
- **Solution**: Use a smaller model (`tiny` or `base`) or enable GPU support if available

### Files not being processed
- **Solution**: Check that:
  - Files are in the correct `SOURCE_DIR`
  - File extensions match `SUPPORTED_EXTENSIONS`
  - Transcripts don't already exist (the script skips duplicates)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **OpenAI Whisper**: The incredible speech recognition model powering this tool  
  [github.com/openai/whisper](https://github.com/openai/whisper)
- **Google Colab**: Free GPU resources for AI experimentation
- Inspired by the need to make speech-to-text accessible to everyone

---

## Further Reading

- [Whisper Paper (arXiv)](https://arxiv.org/abs/2212.04356)
- [Whisper Model Card](https://github.com/openai/whisper/blob/main/model-card.md)
- [OpenAI Whisper Documentation](https://github.com/openai/whisper)

---