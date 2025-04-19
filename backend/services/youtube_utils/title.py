from yt_dlp import YoutubeDL


def get_youtube_title(url: str) -> str:
    """
    Uses yt-dlp to extract the title of a YouTube video.
    """
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title", "Untitled Video")

# Example usage
# if __name__ == "__main__":
#     url = "https://www.youtube.com/watch?v=u-LAZO2WbzQ"
#     try:
#         title = get_youtube_title(url)
#         print(title)
#     except Exception as e:
#         print(f"❌ Failed to get title: {e}")
