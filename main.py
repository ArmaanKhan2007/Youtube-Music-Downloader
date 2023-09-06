import os
from pytube import YouTube
from pytube import Playlist

# ANSI escape codes for text styles and colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"  # Define the BOLD escape code
UNDERLINE = "\033[4m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

# ASCII art saying "Music Downloader"
MUSIC_DOWNLOADER_ART = """
𝖄𝖔𝖚𝖙𝖚𝖇𝖊 𝕸𝖚𝖘𝖎𝖈 𝕯𝖔𝖚𝖓𝖑𝖔𝖆𝖉𝖊𝖗                   
"""

def download_youtube_music(url, output_path='./'):
    try:
        if 'playlist' in url.lower():
            # If the URL is for a playlist, download the entire playlist
            playlist = Playlist(url)
            playlist_title = playlist.title

            # Create a directory with the playlist title
            playlist_dir = os.path.join(output_path, playlist_title)
            os.makedirs(playlist_dir, exist_ok=True)

            for video_url in playlist.video_urls:
                download_youtube_music(video_url, playlist_dir)
        else:
            # Create a YouTube object
            yt = YouTube(url)

            # Get the video title
            video_title = yt.title

            # Create a safe file name by removing characters that are not allowed in file names
            safe_video_title = ''.join(c for c in video_title if c.isalnum() or c in [' ', '_', '-'])

            # Check if the file already exists
            mp3_file_path = os.path.join(output_path, safe_video_title + ".mp3")
            if os.path.exists(mp3_file_path):
                print(f"\nFile already exists: {safe_video_title}.mp3\n")
                return

            # Choose the stream with the best audio quality and mp3 file extension
            stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

            # Download the audio stream directly in MP3 format
            stream.download(output_path, filename=safe_video_title + ".mp3")

            # Terminal formatting for success message
            print(f"\n\n{MUSIC_DOWNLOADER_ART}")
            print(f"\nDownloaded MP3: {safe_video_title}.mp3\n")

    except Exception as e:
        # Terminal formatting for error message
        print(f"\nError: {str(e)}\n")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the terminal screen
    print(f"{MUSIC_DOWNLOADER_ART}")
    print("YouTube Video/Playlist to MP3 Downloader\n")

    while True:
        print("Options:")
        print("1. Download a single video")
        print("2. Download a playlist")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            video_url = input("Enter the YouTube video URL: ")
            download_youtube_music(video_url)
        elif choice == '2':
            playlist_url = input("Enter the YouTube playlist URL: ")
            download_youtube_music(playlist_url)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
