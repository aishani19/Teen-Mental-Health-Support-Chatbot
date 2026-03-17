def coping_suggestions(topic):

    suggestions = {

        "career": [
            "Break DSA practice into small daily goals.",
            "Focus on understanding patterns rather than solving many problems.",
            "Take breaks to avoid burnout."
        ],

        "study": [
            "Try studying in short focused sessions like the Pomodoro technique.",
            "Prioritize important topics instead of trying to study everything at once."
        ],

        "family": [
            "Writing your thoughts before talking can help organize feelings.",
            "Talking to a trusted adult or counselor can help."
        ],

        "peer": [
            "Try to focus on your own progress rather than comparisons.",
            "Healthy boundaries with friends are important."
        ],

        "confidence": [
            "Progress takes time, and it's okay to learn at your own pace.",
            "Focus on small wins to rebuild confidence."
        ],

        "general": [
            "Taking a short walk or break can help calm your mind.",
            "Talking through problems often helps clarify them."
        ]
    }

    return suggestions.get(topic, suggestions["general"])
import random

def chatbot_reply(text):

    emotion = detect_emotion(text)
    topic = detect_topic(text)

    suggestions = coping_suggestions(topic)
    suggestion = random.choice(suggestions)

    prompt = f"""
    You are a supportive AI assistant for students.

    Emotion detected: {emotion}
    Topic: {topic}

    User message: {text}

    Include this coping suggestion naturally:
    {suggestion}
    """

    response = generate_llm_response(prompt)

    return response