"""
LLM call utilities for recipe blog generation.
"""
from app.clients.openai_client import OpenAIClient
from app.utils.logging import setup_logger

logger = setup_logger()


def call_openai_chat(
        messages: list[dict],
        temperature: float = 0.7,
        max_tokens: int = 1000
) -> str:
    client = OpenAIClient()
    try:
        return client.chat(messages, temperature=temperature, max_tokens=max_tokens)
    except Exception as e:
        logger.error("OpenAI API call failed: %s", e, exc_info=True)
        return "[Error: OpenAI API call failed. See logs for details.]"
