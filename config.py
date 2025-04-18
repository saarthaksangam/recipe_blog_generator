from datetime import datetime

BLOG_NAME = "Platin' It with Wendy"
TAGLINE = "Recipes that impress with ease"
MODEL_NAME = "gpt-4.1"

def today_string():
    return datetime.now().strftime("%B %d, %Y")

def today_for_filename():
    return datetime.now().strftime("%Y-%m-%d")
