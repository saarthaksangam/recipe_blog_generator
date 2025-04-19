"""
Prompt template loader for recipe blog generator.
"""
from pathlib import Path


def load_prompt_template(name: str) -> str:
    """Loads a prompt template from generator/prompts/*.md or .txt"""
    from generator.logging_utils import setup_logger
    logger = setup_logger()
    path = Path(__file__).resolve().parent.parent / "prompts" / name
    try:
        return path.read_text()
    except Exception as e:
        logger.error("Failed to read prompt template %s: %s", path, e, exc_info=True)
        return f"[Error: Failed to load prompt template: {name}]"
