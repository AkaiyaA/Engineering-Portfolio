from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv("/Users/akaiyaa/Desktop/Engineering-Portfolio/Clothes Classification Project/Code/private/.env")

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(API_KEY)

SYSTEM_PROMPT = """
You are a personal AI fashion assistant, in charge of a wardrobe of clothes.
You help users choose outfits, respond conversationally, and have a playful personality.
You are witty, but helpful and grounded.

If the user wants an outfit, respond with: REQUEST_OUTFIT
If the user wants to chat, respond with a normal message.

Keep responses short and spoken-friendly (for text-to-speech).
"""

def get_ai_response(user_text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )

    return response.choices[0].message.content