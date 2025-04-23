import os

# Your Groq API key (must be set in the environment)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("Set the GROQ_API_KEY environment variable")

# Which model to call – you can change this
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# OpenAI‑compatible endpoint for chat completions
GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"  # :contentReference[oaicite:1]{index=1}
