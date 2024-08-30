from pytube import Playlist
from pytube import YouTube
import os

# Meminta input URL dari pengguna
playlist_url = input("Masukkan URL playlist: ")

# Inisialisasi Playlist
playlist = Playlist(playlist_url)

# Cetak informasi dasar tentang playlist
print(f"\nNama Playlist: {playlist.title}")
print(f"Jumlah Video: {len(playlist.videos)}\n")

# Mendapatkan URL masing-masing video dalam playlist
video_urls = playlist.video_urls

# Cetak daftar URL
# print("Daftar URL video dalam playlist:")
# for idx, url in enumerate(video_urls, start=1):
#     print(f"{idx}. {url}")
video_urls = list(video_urls)
# print(video_urls)
# URL dari video YouTube
for url in video_urls:
    

# Buat objek YouTube
    yt = YouTube(url)

# Pilih stream audio
    audio_stream = yt.streams.filter(only_audio=True).first()

# Unduh dan simpan sebagai file MP4 (default)
    audio_file = audio_stream.download()
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)

    print(f"Audio telah diunduh dan disimpan sebagai {new_file}")
