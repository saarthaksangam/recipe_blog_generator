from generator.batch_processor import process_all_srt
from config import INPUT_DIR
import sys
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))

def main():
    process_all_srt(INPUT_DIR)

if __name__ == "__main__":
    main()