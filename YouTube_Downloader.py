from pytube import YouTube

# List of YouTube video URLs you want to download
video_urls = [
    "https://www.youtube.com/watch?v=NCvI-K0Gp90"
    # Add more video URLs here
]

# Provide the path to the folder where you want to store the downloaded videos
download_folder = "./ytDownload"

# Iterate over each video URL
for url in video_urls:
    # Create a YouTube object and extract the video
    yt = YouTube(url)
    video = yt.streams.first()

    # Download the video to the specified folder
    video.download(download_folder)

    print(f"Video '{yt.title}' downloaded successfully!")

print("All videos downloaded!")