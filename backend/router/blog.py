# backend/router/blog.py

from fastapi import APIRouter, Query, HTTPException
from backend.agents.blog_agent import blog_agent
from agents import Runner
from backend.schemas.v1.blog import BlogPost  # Pydantic model (you'll create this next)

router = APIRouter()


@router.get("/generate-blog", response_model=BlogPost)
async def generate_blog(youtube_url: str = Query(..., description="Full YouTube video URL")):
    if not "youtube.com/watch" in youtube_url and not "youtu.be" in youtube_url:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL format")
    result = await Runner.run(blog_agent, input=youtube_url)
    return result.final_output
