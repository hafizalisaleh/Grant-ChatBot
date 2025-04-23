import requests
from .config import GROQ_API_KEY, GROQ_MODEL, GROQ_CHAT_URL

def call_groq_chat(messages: list) -> dict:
    """
    Send a chat completion request to Groq and return the parsed JSON response.
    messages: list of {"role": "...", "content": "..."}
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": messages
    }
    resp = requests.post(GROQ_CHAT_URL, json=payload, headers=headers)
    resp.raise_for_status()  # blow up if anything went wrong
    return resp.json()
