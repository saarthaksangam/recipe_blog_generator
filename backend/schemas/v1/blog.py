# backend/schemas/blog.py

from pydantic import BaseModel

class BlogPost(BaseModel):
    title: str
    markdown: str
    upload_date: str
    thumbnail_url: str
    youtube_url: str
