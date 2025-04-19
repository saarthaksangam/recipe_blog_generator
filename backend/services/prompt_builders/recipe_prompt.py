from backend.services.prompt_builders import load_prompt_template
from backend.utils.helpers import today_string
from config import BLOG_NAME, TAGLINE


def build_recipe_prompt_messages(
        youtube_title: str,
        transcript: str,
        thumbnail_url: str,
        video_id: str,
        upload_date: str = None
) -> list[dict]:
    """
    Builds system and user messages for generating the full blog post.
    Includes thumbnail, embedded video, and dynamic config like blog name and tagline.
    """
    upload_date = upload_date or today_string()

    # Load templates
    system_template = load_prompt_template("system/recipe_prompt.md")
    user_template = load_prompt_template("user/recipe_prompt.md")

    # 🔧 Fill in system prompt
    filled_system_prompt = (
        system_template
        .replace("{{blog_name}}", BLOG_NAME)
        .replace("{{tagline}}", TAGLINE)
        .strip()
    )

    # 🔧 Fill in user prompt
    filled_user_prompt = (
        user_template
        .replace("{{title}}", youtube_title)
        .replace("{{title_lower}}", youtube_title.lower())
        .replace("{{upload_date}}", upload_date)
        .replace("{{tagline}}", TAGLINE)
        .replace("{{blog_name}}", BLOG_NAME)
        .replace("{{thumbnail_url}}", thumbnail_url)
        .replace("{{video_id}}", video_id)
        .replace("{{transcript}}", transcript)
        .strip()
    )

    return [
        {"role": "system", "content": filled_system_prompt},
        {"role": "user", "content": filled_user_prompt}
    ]
