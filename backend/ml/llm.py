import os
from groq import Groq
from dotenv import load_dotenv

# load env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)


def generate_llm_response(prompt: str) -> str:
    try:

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ UPDATED MODEL
            messages=[
                {
                    "role": "system",
                    "content": "You are a compassionate mental health support chatbot for teenagers."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        print("Groq Error:", e)
        return "I'm sorry, I couldn't generate a response right now. Please try again."