from pathlib import Path


def load_prompt_template(name: str) -> str:
    """Loads a prompt template from generator/prompts/*.md or .txt"""
    path = Path(__file__).resolve().parent.parent / "prompts" / name
    return path.read_text()
