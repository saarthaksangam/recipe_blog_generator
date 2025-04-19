# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.middleware.logging import log_requests
from backend.router import blog

app = FastAPI(
    title="Recipe Blog Generator API",
    description="Convert YouTube cooking video transcripts into structured, high-quality recipe blog posts using LLMs.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Recipe Blog Generator API 👩‍🍳",
        "docs": "/docs",
        "generate_blog": "/api/v1/generate-blog?youtube_url=https://..."
    }


# Middleware
app.middleware("http")(log_requests)

# Routes
app.include_router(blog.router, prefix="/api/v1", tags=["Blog"])
