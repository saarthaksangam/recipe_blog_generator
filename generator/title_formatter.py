from pathlib import Path


def build_title_prompt(raw_filename: str) -> str:
    prompt_path = Path(__file__).resolve().parent.parent / "prompts" / "clean_title_prompt.txt"
    prompt_template = prompt_path.read_text()
    return prompt_template.replace("{filename}", raw_filename)
