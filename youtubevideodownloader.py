import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
  
    root = tk.Tk()
    root.withdraw() 

    url = input("Enter the YouTube video URL: ")

    save_path = filedialog.askdirectory(title="Select Download Folder")

    if url and save_path:
        download_video(url, save_path)
    else:
        print("URL or save path not provided.")

if __name__ == "__main__":
    main()
