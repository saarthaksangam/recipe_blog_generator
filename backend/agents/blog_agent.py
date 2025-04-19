from agents import Agent

from backend.services.tools.blog_post_tool import generate_blog_from_youtube

from backend.schemas.v1.blog import BlogPost

blog_agent = Agent(
    name="YouTubeRecipeAgent",
    instructions="Generate a full recipe blog post using a YouTube video's transcript and thumbnail.",
    tools=[generate_blog_from_youtube],
    output_type=BlogPost,
)
