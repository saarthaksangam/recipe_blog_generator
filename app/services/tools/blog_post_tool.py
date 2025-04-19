from urllib.parse import urlparse, parse_qs

from agents import function_tool

from app.services.llm_calls import call_openai_chat
from app.services.prompt_builders.recipe_prompt import build_recipe_prompt_messages
from app.services.youtube_utils.cleaner import strip_vtt_metadata
from app.services.youtube_utils.thumbnail import get_thumbnail_from_youtube
from app.services.youtube_utils.title import get_youtube_title
from app.services.youtube_utils.transcript import get_srt_from_youtube
from app.utils.helpers import sanitize_filename, today_for_filename
from app.utils.logging import setup_logger
from config import OUTPUT_DIR

logger = setup_logger()


def extract_video_id(url: str) -> str:
    """Extracts the YouTube video ID from a full URL."""
    query = urlparse(url).query
    return parse_qs(query).get("v", [""])[0]  # fallback empty string if not found


@function_tool
def generate_blog_from_youtube(url: str) -> str:
    """
    Full pipeline to generate a recipe blog post from a YouTube video URL.
    - Extracts transcript, thumbnail, video ID, title
    - Generates full blog post via OpenAI
    - Saves post using sanitized YouTube title as filename
    """
    # Step 1: Get YouTube metadata
    try:
        youtube_title = get_youtube_title(url)
        safe_filename = sanitize_filename(youtube_title)
        video_id = extract_video_id(url)
    except Exception as e:
        return f"❌ Failed to fetch YouTube metadata. Error: {e}"

    # Step 2: Check if file already exists
    output_folder = OUTPUT_DIR / safe_filename
    output_filename = f"{safe_filename} - {today_for_filename()}.md"
    output_path = output_folder / output_filename

    if output_path.exists():
        logger.info("⏭️  Skipping (already exists): %s", output_path)
        return f"✅ Blog post already exists at: {output_path}"

    # Step 3: Download thumbnail
    try:
        thumbnail_url = get_thumbnail_from_youtube(url)
    except Exception as e:
        thumbnail_url = ""
        logger.warning("⚠️ Failed to fetch thumbnail: %s", e)

    # Step 4: Download and clean transcript
    try:
        raw_transcript = get_srt_from_youtube(url)
        transcript = strip_vtt_metadata(raw_transcript)
    except Exception as e:
        return f"❌ Failed to retrieve subtitles. Error: {e}"

    # Step 5: Generate full blog post
    recipe_messages = build_recipe_prompt_messages(
        youtube_title=youtube_title,
        transcript=transcript,
        thumbnail_url=thumbnail_url,
        video_id=video_id
    )

    blog_post = call_openai_chat(recipe_messages, temperature=0.7, max_tokens=5000)

    # Step 6: Save blog post
    output_folder.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(blog_post.strip())

    return blog_post.strip()
