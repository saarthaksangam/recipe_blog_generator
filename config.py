from datetime import datetime
from pathlib import Path

BLOG_NAME = "Platin' It with Wendy"
TAGLINE = "Recipes that impress with ease"
MODEL_NAME = "gpt-4.1-2025-04-14"

PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_DIR = PROJECT_ROOT / "input_transcripts"
OUTPUT_DIR = PROJECT_ROOT / "generated_posts"

def today_string():
    return datetime.now().strftime("%B %d, %Y")

def today_for_filename():
    return datetime.now().strftime("%Y-%m-%d")
