import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from config import MODEL_NAME

load_dotenv()


def generate_blog_post(prompt: str) -> str:
    response = client.chat.completions.create(model=MODEL_NAME,
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=1500)
    return response.choices[0].message.content
