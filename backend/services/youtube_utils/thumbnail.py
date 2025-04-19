from yt_dlp import YoutubeDL


def get_thumbnail_from_youtube(url: str) -> str:
    """
    Uses yt-dlp to extract the thumbnail URL from a YouTube video (forces .jpg if needed).
    """
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        thumbnail = info.get("thumbnail", "")
        return (
            thumbnail.replace("vi_webp", "vi").replace(".webp", ".jpg")
            if thumbnail else ""
        )

# Example usage
# if __name__ == "__main__":
#     url = "https://www.youtube.com/watch?v=u-LAZO2WbzQ"
#     try:
#         thumbnail_url = get_thumbnail_from_youtube(url)
#         print(thumbnail_url)
#     except Exception as e:
#         print(f"❌ Failed to get thumbnail: {e}")
