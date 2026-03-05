"""LLM chat client factory - uses first available provider from .env."""
import os


def create_chat_client():
    """Create chatlas client from ANTHROPIC_API_KEY, OPENAI_API_KEY, GOOGLE_API_KEY, or GITHUB_TOKEN in .env."""
    system_prompt = (
        # TODO: Update
        "You are a helpful assistant for a non-market housing dashboard in Vancouver. "
        "Help users understand the data, filters, and visualizations. Be concise and informative."
    )
    if os.getenv("ANTHROPIC_API_KEY"):
        from chatlas import ChatAnthropic
        return ChatAnthropic(
            model="claude-haiku-4-5-20251001",
            system_prompt=system_prompt,
        )
    if os.getenv("OPENAI_API_KEY"):
        from chatlas import ChatOpenAI
        return ChatOpenAI(
            model="gpt-5-nano",
            system_prompt=system_prompt,
        )
    if os.getenv("GOOGLE_API_KEY"):
        from chatlas import ChatGoogle
        return ChatGoogle(
            model="gemini-3.1-flash-lite-preview",
            system_prompt=system_prompt,
        )
    if os.getenv("GITHUB_TOKEN"):
        from chatlas import ChatGithub
        return ChatGithub(
            model="openai/gpt-4o-mini",
            system_prompt=system_prompt,
        )
    return None
