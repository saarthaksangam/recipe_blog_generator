import os
import tempfile

from yt_dlp import YoutubeDL


def get_srt_from_youtube(url: str) -> str:
    """
    Extract auto-generated English subtitles from a YouTube video using yt-dlp.
    Supports .vtt and .srt formats (prefers .srt).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        ydl_opts = {
            "skip_download": True,
            "writeautomaticsub": True,
            "subtitleslangs": ["en"],
            "subtitlesformat": "srt",  # will fallback to vtt if srt not available
            "outtmpl": f"{tmpdir}/%(id)s.%(ext)s",
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            video_id = info["id"]

        # Try srt first
        srt_path = os.path.join(tmpdir, f"{video_id}.en.srt")
        vtt_path = os.path.join(tmpdir, f"{video_id}.en.vtt")

        if os.path.exists(srt_path):
            with open(srt_path, "r", encoding="utf-8") as f:
                return f.read()
        elif os.path.exists(vtt_path):
            with open(vtt_path, "r", encoding="utf-8") as f:
                return f.read()
        else:
            raise RuntimeError("No English subtitles (.srt or .vtt) found for this video.")

# Example usage
# if __name__ == "__main__":
#     url = "https://www.youtube.com/watch?v=u-LAZO2WbzQ"
#     try:
#         srt = get_srt_from_youtube(url)
#         print(srt)
#     except Exception as e:
#         print(f"❌ Failed to get subtitles: {e}")
