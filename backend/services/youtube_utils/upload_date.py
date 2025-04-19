from yt_dlp import YoutubeDL

def get_youtube_upload_date(youtube_url: str) -> str:
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
        'forcejson': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        upload_date = info.get('upload_date')  # Format: YYYYMMDD

    # Optional: format to YYYY-MM-DD
    if upload_date:
        return f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"
    else:
        return "Unknown"

# Example usage
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=u-LAZO2WbzQ"
    try:
        upload_date = get_youtube_upload_date(url)
        print(upload_date)
    except Exception as e:
        print(f"❌ Failed to get upload date: {e}")
