"""
Prompt builder for recipe title generation.
"""
from app.services.prompt_builders import load_prompt_template


def build_title_prompt_messages(filename: str) -> list[dict]:
    system_template = load_prompt_template("system/title_prompt.md")
    user_template = load_prompt_template("user/title_prompt.md")

    system_prompt = system_template.strip()
    user_prompt = user_template.replace("{{filename}}", filename).strip()

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
