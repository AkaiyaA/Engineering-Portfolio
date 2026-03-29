from pathlib import Path
from dotenv import load_dotenv
import os
from openai import OpenAI

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path, override=True)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(f"API key not found. Looked in: {env_path}")

def get_client():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Check .env loading.")

    return OpenAI(api_key=api_key)


SYSTEM_PROMPT = """
Your name is Pandora. 
You are a personal AI closet assistant in charge of a wardrobe of clothes, and clothing management / recommendation.
You help users choose outfits, respond conversationally, and have a analytical personality.
You are witty, but helpful and grounded.

If the user wants an outfit, respond with: REQUEST_OUTFIT
If the user wants to chat, respond with a normal message.

Keep responses short and spoken-friendly (for text-to-speech).
"""

def get_ai_response(user_text):
    client = get_client()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )

    return response.choices[0].message.content