from pathlib import Path
from generator.transcript_parser import extract_transcript_from_srt
from generator.recipe_formatter import build_recipe_prompt
from generator.openai_client import generate_blog_post
from generator.utils import sanitize_filename
from config import today_for_filename, INPUT_DIR, OUTPUT_DIR

def process_single_srt(srt_path: Path):
    recipe_title = srt_path.stem.replace("_", " ").replace("-", " ").title()
    safe_title = sanitize_filename(recipe_title)
    output_folder = OUTPUT_DIR / safe_title
    output_folder.mkdir(parents=True, exist_ok=True)

    output_filename = f"{safe_title} - {today_for_filename()}.md"
    output_path = output_folder / output_filename

    if output_path.exists():
        print(f"⏭️  Skipping already processed: {output_path}")
        return

    transcript = extract_transcript_from_srt(srt_path)
    prompt = build_recipe_prompt(transcript, title=recipe_title)
    blog_post = generate_blog_post(prompt)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(blog_post)

    print(f"✅ Blog post saved: {output_path}")

def process_all_srt(transcript_dir: Path):
    if not transcript_dir.exists():
        print(f"❌ Input folder not found: {transcript_dir}")
        print("📁 Please create it and drop your .srt files inside.")
        return
    srt_files = list(transcript_dir.glob("*.srt"))
    if not srt_files:
        print("⚠️ No .srt files found.")
        return

    for srt_path in srt_files:
        process_single_srt(srt_path)
