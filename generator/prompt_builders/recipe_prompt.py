from generator.prompt_builders import load_prompt_template
from config import BLOG_NAME, TAGLINE
from generator.utils import today_string

def build_recipe_prompt(transcript: str, title: str) -> str:
    today = today_string()
    template = load_prompt_template("recipe_prompt_template.md")

    return (
        template
        .replace("{{title}}", title)
        .replace("{{date}}", today)
        .replace("{{transcript}}", transcript)
        .replace("{{blog_name}}", BLOG_NAME)
        .replace("{{tagline}}", TAGLINE)
        .strip()
    )