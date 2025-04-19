"""
LLM call utilities for recipe blog generation.
"""
from generator.openai_client import OpenAIClient


def call_openai_chat(
    messages: list[dict],
    temperature: float = 0.7,
    max_tokens: int = 1000
) -> str:
    client = OpenAIClient()
    return client.chat(messages, temperature=temperature, max_tokens=max_tokens)
