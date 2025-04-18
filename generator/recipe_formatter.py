from config import BLOG_NAME, TAGLINE, today_string
from pathlib import Path

def build_recipe_prompt(transcript: str, title: str) -> str:
    today = today_string()

    template_path = Path(__file__).resolve().parent.parent / "prompts" / "recipe_prompt_template.md"
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Simple templating (you could swap in Jinja2 later if needed)
    prompt = (
        template
        .replace("{{title}}", title)
        .replace("{{date}}", today)
        .replace("{{transcript}}", transcript)
    )

    return f"""
    You are a food blogger writing clear, warm, and delicious recipe blog posts for a blog called "{BLOG_NAME}" — tagline: *{TAGLINE}*.

    Please generate the recipe blog post using the **Markdown structure shown below**. 
    - Every section must use Markdown headers (`#`, `##`, `###`).
    - Do not skip or change heading levels.
    - Your output should match the formatting and section names exactly.
    - Do not summarize or alter the structure in your own words.

    {prompt}
    """
