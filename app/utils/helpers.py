"""
Utility functions for string sanitization and date formatting.
"""
import re
from datetime import datetime
import re

def sanitize_filename(name: str) -> str:
    # Remove illegal characters (Windows-safe)
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace multiple spaces with a single space
    name = re.sub(r'\s+', ' ', name)
    # Strip leading/trailing spaces
    name = name.strip()
    return name



def today_string():
    return datetime.now().strftime("%B %d, %Y")


def today_for_filename():
    return datetime.now().strftime("%Y-%m-%d")
