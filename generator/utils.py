from datetime import datetime


def sanitize_filename(name: str) -> str:
    return "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).rstrip()

def today_string():
    return datetime.now().strftime("%B %d, %Y")


def today_for_filename():
    return datetime.now().strftime("%Y-%m-%d")
