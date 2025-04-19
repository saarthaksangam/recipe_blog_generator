import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.agents.blog_agent import blog_agent
from agents import Runner
import asyncio


async def main():
    url = input("🎥 Enter YouTube URL: ")
    if not url:
        # Default URL for testing
        url = "https://www.youtube.com/watch?v=u-LAZO2WbzQ"
    result = await Runner.run(blog_agent, input=url)

    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
