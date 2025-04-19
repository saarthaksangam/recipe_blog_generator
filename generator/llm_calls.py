from generator.openai_client import OpenAIClient


def call_openai_chat(system_prompt: str, user_prompt: str, temperature=0.7, max_tokens=1000) -> str:
    client = OpenAIClient()
    return client.chat(system_prompt, user_prompt, temperature=temperature, max_tokens=max_tokens)
