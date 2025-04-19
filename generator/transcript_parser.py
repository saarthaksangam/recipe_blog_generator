"""
Transcript parsing utilities for extracting dialogue from SRT files.
"""
import re


def extract_transcript_from_srt(srt_path: str) -> str:
    with open(srt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    dialogue_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.isdigit() or re.match(r"\d{2}:\d{2}:\d{2},\d{3}", line):
            continue
        dialogue_lines.append(line)

    return " ".join(dialogue_lines)
