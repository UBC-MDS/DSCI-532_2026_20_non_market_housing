"""LLM chat client factory - uses first available provider from .env."""
import os


def get_querychat_client():
    """Create chatlas client for querychat from first available provider in .env.
    Uses ANTHROPIC_API_KEY, OPENAI_API_KEY, GOOGLE_API_KEY, or GITHUB_TOKEN."""
    if os.getenv("ANTHROPIC_API_KEY"):
        from chatlas import ChatAnthropic
        return ChatAnthropic(model="claude-haiku-4-5-20251001")
    if os.getenv("OPENAI_API_KEY"):
        from chatlas import ChatOpenAI
        return ChatOpenAI(model="gpt-5-nano")
    if os.getenv("GOOGLE_API_KEY"):
        from chatlas import ChatGoogle
        return ChatGoogle(model="gemini-3.1-flash-lite-preview")
    if os.getenv("GITHUB_TOKEN"):
        from chatlas import ChatGithub
        return ChatGithub(model="openai/gpt-4o-mini")
    return None