import tkinter as tk
from pytube import Playlist, YouTube
import os

def get_playlist_url():
    url = entry.get()
    video_urls = list(Playlist(url).video_urls)
    download_mp3(video_urls)
    label.config(text="Download Complete!")

def download_mp3(video_urls):
    for url in video_urls:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file = audio_stream.download()
        base, ext = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        os.rename(audio_file, new_file)

root = tk.Tk()
root.title("YouTube Playlist MP3 Downloader")

label = tk.Label(root, text="Enter Playlist URL:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Download", command=get_playlist_url)
button.pack()

root.mainloop()
