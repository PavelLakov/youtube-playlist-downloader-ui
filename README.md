[![Live Demo](https://img.shields.io/badge/Live-Demo-orange)](https://huggingface.co/spaces/pavellakov/youtube-playlist-downloader)

# 🎬 YouTube Playlist Downloader (Gradio UI)

This is a simple, cross-platform GUI application for downloading **YouTube playlists** as either **MP4 videos** or **MP3 audio**, built using [Gradio](https://gradio.app/) and [yt-dlp](https://github.com/yt-dlp/yt-dlp).


---

## ✨ Features

- ✅ Paste any YouTube playlist URL
- ✅ Choose between **MP4** (video) or **MP3** (audio)
- ✅ Download happens as a ZIP via browser
- ✅ Runs in your browser with an interactive interface
- ✅ No console needed

---

## 🚀 How to Run

### 1. Clone or download this project

```
git clone https://github.com/yourname/youtube-playlist-downloader-gradio.git
cd youtube-playlist-downloader-gradio
```



### 2. Create and activate a virtual environment (optional but recommended)

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

This will launch the Gradio interface in your browser at:  
**`http://127.0.0.1:7860`**

---

## 🛠 Requirements

- Python 3.8 or newer
- [FFmpeg](https://ffmpeg.org/download.html) installed and in your system PATH (for audio conversion)

---

## 📦 File Structure

```
├── app.py              # Main Python GUI app
├── requirements.txt    # Required Python packages
├── readme.txt          # Basic text instructions
└── readme.md           # Full Markdown documentation
```

---

## 🔒 Legal Notice

This tool is for **personal and educational use only**. Downloading videos from YouTube may violate their terms of service. Make sure you have permission to download any content you access using this tool.

---

## 🧑‍💻 Author

Pavel Lakov  
MIT License
