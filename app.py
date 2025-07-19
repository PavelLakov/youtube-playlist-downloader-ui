import yt_dlp
import os
import gradio as gr
import subprocess

def pick_folder():
    try:
        script = """tell application \"System Events\"
            activate
            set theFolder to POSIX path of (choose folder with prompt \"Choose a folder to save downloads:\")
        end tell"""
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def download_playlist(url, download_type, folder_path):
    folder = folder_path or "downloads"
    os.makedirs(folder, exist_ok=True)

    if download_type == "Video (MP4)":
        opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        }
    else:
        opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        return f"✅ Download complete. Saved in: {os.path.abspath(folder)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

with gr.Blocks(title="🎬 YouTube Playlist Downloader", theme=gr.themes.Base()) as app:
    gr.Markdown("## 📥 YouTube Playlist Downloader")
    gr.Markdown("Paste a YouTube playlist URL, choose format, and select your download folder.")

    with gr.Row():
        url = gr.Textbox(label="🔗 Playlist URL", placeholder="https://youtube.com/playlist?list=...")
        format_choice = gr.Radio(["Video (MP4)", "Audio (MP3)"], label="🎞 Download Type", value="Video (MP4)")

    with gr.Row():
        folder_path = gr.Textbox(label="📁 Download Folder", interactive=True)
        choose_button = gr.Button("📂 Choose Folder")
        choose_button.click(fn=pick_folder, inputs=[], outputs=folder_path)

    with gr.Row():
        download_button = gr.Button("⬇️ Download Playlist", variant="primary")

    output_msg = gr.Textbox(label="📊 Status", lines=4, interactive=False)

    download_button.click(
        fn=download_playlist,
        inputs=[url, format_choice, folder_path],
        outputs=output_msg
    )

app.launch(inbrowser=True)
