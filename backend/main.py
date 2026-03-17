from fastapi import FastAPI
from schemas import ChatRequest

from ml.classifier import detect_emotion, detect_topic
from ml.memory import build_history
from ml.coping import coping_suggestions
from ml.llm import generate_llm_response

from services.safety import detect_crisis, CRISIS_RESPONSE

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
def chat(data: ChatRequest):

    message = data.message
    history = data.history

    # 🚨 CRISIS DETECTION (highest priority)
    if detect_crisis(message):
        return {
            "reply": CRISIS_RESPONSE,
            "emotion": "crisis",
            "topic": "safety"
        }

    # Emotion detection
    emotion = detect_emotion(message)

    # Topic detection
    topic = detect_topic(message)

    # Build conversation memory
    history_text = build_history(history)

    # Get coping suggestions
    suggestions = coping_suggestions(topic)

    # Build prompt for LLM
    prompt = f"""
You are a compassionate mental health support chatbot for teenagers.

Conversation history:
{history_text}

User message:
{message}

Detected emotion: {emotion}
Detected topic: {topic}

Helpful coping suggestions:
{suggestions}

Instructions:
- Respond empathetically.
- Validate the user's feelings.
- Provide practical coping advice when appropriate.
- Avoid repeating previous responses.
- Ask one supportive follow-up question.
"""

    # Generate response from LLM
    reply = generate_llm_response(prompt)

    return {
        "reply": reply,
        "emotion": emotion,
        "topic": topic
    }