"""
Prompt builder for recipe blog post generation.
"""

from config import BLOG_NAME, TAGLINE
from generator.prompt_builders import load_prompt_template
from generator.utils import today_string


def build_recipe_prompt_messages(title: str, transcript: str) -> list[dict]:
    today = today_string()

    system_template = load_prompt_template("system/recipe_prompt.md")
    user_template = load_prompt_template("user/recipe_prompt.md")

    system_prompt = (
        system_template
        .replace("{{blog_name}}", BLOG_NAME)
        .replace("{{tagline}}", TAGLINE)
    )

    user_prompt = (
        user_template
        .replace("{{title}}", title)
        .replace("{{date}}", today)
        .replace("{{tagline}}", TAGLINE)
        .replace("{{title_lower}}", title.lower())
        .replace("{{transcript}}", transcript)
    )

    return [
        {"role": "system", "content": system_prompt.strip()},
        {"role": "user", "content": user_prompt.strip()}
    ]
