CRISIS_KEYWORDS = [
    "kill myself",
    "suicide",
    "want to die",
    "harm myself",
    "hurt myself",
    "end my life",
    "i don't want to live",
    "i feel like harming myself"
]

CRISIS_RESPONSE = """
I'm really sorry that you're feeling this way. Thoughts about harming yourself are very serious, and you deserve immediate support.

Your safety matters and you do not have to face this alone.

If these thoughts feel overwhelming, please reach out to someone you trust such as a friend, family member, teacher, or counselor.

You can also contact the **Kiran Mental Health Helpline (India) – 1800-599-0019**, available 24/7.

If you feel like you might act on these thoughts or are in immediate danger, please seek emergency help right away or go somewhere safe where someone can support you.

If you want, you can share what has been making things feel this difficult today. I'm here to listen.
"""

def detect_crisis(text: str) -> bool:
    text = text.lower()

    for word in CRISIS_KEYWORDS:
        if word in text:
            return True

    return False