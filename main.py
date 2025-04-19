# main.py (CLI entry point, optional)

import sys
from pathlib import Path
import asyncio

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent / "backend"))

from backend.agents.blog_agent import blog_agent
from agents import Runner

async def main():
    url = input("🎥 Enter YouTube URL: ")
    if not url:
        url = "https://www.youtube.com/watch?v=u-LAZO2WbzQ"
    result = await Runner.run(blog_agent, input=url)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
