"""
OpenAI client wrapper for chat-based LLM calls.
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

from config import MODEL_NAME

load_dotenv()


class OpenAIClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        return cls._instance

    def chat(
            self,
            messages: list[dict],
            temperature: float = 0.7,
            max_tokens: int = 1000
    ) -> str:
        try:
            response = self._client.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            from app.utils.logging import setup_logger
            logger = setup_logger()
            logger.error("OpenAI chat() failed: %s", e, exc_info=True)
            raise
