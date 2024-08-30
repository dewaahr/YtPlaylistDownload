from pytube import Playlist
from pytube import YouTube
import os

playlist_url = input("Masukkan URL playlist: ")

playlist = Playlist(playlist_url)
print(f"\nNama Playlist: {playlist.title}")
print(f"Jumlah Video: {len(playlist.videos)}\n")

video_urls = playlist.video_urls

# print("Daftar URL video dalam playlist:")
# for idx, url in enumerate(video_urls, start=1):
#     print(f"{idx}. {url}")
video_urls = list(video_urls)
# print(video_urls)
for url in video_urls:
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download()
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    
    print(f"Audio telah diunduh dan disimpan sebagai {new_file}")
