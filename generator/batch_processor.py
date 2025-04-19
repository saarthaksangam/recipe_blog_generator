from pathlib import Path

from config import OUTPUT_DIR
from generator.llm_calls import call_openai_chat
from generator.prompt_builders.recipe_prompt import build_recipe_prompt_messages
from generator.prompt_builders.title_prompt import build_title_prompt_messages
from generator.transcript_parser import extract_transcript_from_srt
from generator.utils import sanitize_filename, today_for_filename


def process_single_srt(srt_path: Path):
    raw_filename = srt_path.stem

    # 🔮 Step 1: Use LLM to get cleaned blog title
    title_messages = build_title_prompt_messages(raw_filename)
    recipe_title = call_openai_chat(title_messages, temperature=0.0, max_tokens=150)
    safe_title = sanitize_filename(recipe_title)

    # 📂 Step 2: Rename .srt file to cleaned version
    new_srt_name = f"{safe_title}.srt"
    new_srt_path = srt_path.with_name(new_srt_name)

    if srt_path != new_srt_path:
        srt_path.rename(new_srt_path)
        print(f"📄 Renamed input file: {srt_path.name} → {new_srt_name}")
        srt_path = new_srt_path

    # 📝 Step 3: Prepare output paths using cleaned title
    output_folder = OUTPUT_DIR / safe_title
    output_folder.mkdir(parents=True, exist_ok=True)

    output_filename = f"{safe_title} - {today_for_filename()}.md"
    output_path = output_folder / output_filename

    if output_path.exists():
        print(f"⏭️  Skipping already processed: {output_path}")
        return

    # 📜 Step 4: Extract transcript and build prompt
    transcript = extract_transcript_from_srt(srt_path)
    recipe_messages = build_recipe_prompt_messages(recipe_title, transcript)
    blog_post = call_openai_chat(recipe_messages, temperature=0.7, max_tokens=5000)

    # 💾 Step 5: Save generated blog post
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
