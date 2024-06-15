from pytube import YouTube
from moviepy.editor import *

def download_youtube_video_as_mp3(youtube_url, output_path):
    # 使用 pytube 下載 YouTube 視頻
    yt = YouTube(youtube_url)
    video_stream = yt.streams.filter(only_audio=True).first()
    downloaded_file = video_stream.download(output_path=output_path)

    # 使用 moviepy 將下載的視頻文件轉換為 MP3
    audio_clip = AudioFileClip(downloaded_file)
    mp3_filename = downloaded_file.replace('.mp4', '.mp3')
    audio_clip.write_audiofile(mp3_filename)

    # 刪除原始的視頻文件
    audio_clip.close()
    os.remove(downloaded_file)

    print(f"下載並轉換完成: {mp3_filename}")

# 使用範例
youtube_url = 'https://youtu.be/46HaUZSkJDY?si=yCVlFmtcFFh7tx0c'
output_path = 'OneDrive\git_repo\group6_project\huixin_pygame_pt'
download_youtube_video_as_mp3(youtube_url, output_path)
