import re


def strip_vtt_metadata(vtt_text: str) -> str:
    """
    Strips timestamps, cue numbers, and blank lines from .vtt subtitle content.
    """
    lines = []
    for line in vtt_text.splitlines():
        line = line.strip()
        if line == "" or "-->" in line or re.match(r"^\d+$", line):
            continue
        lines.append(line)
    return " ".join(lines)
