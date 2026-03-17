import streamlit as st
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Flexible imports
try:
    from backend.ml.classifier import detect_emotion, detect_topic
    from backend.ml.memory import build_history
    from backend.ml.coping import coping_suggestions
    from backend.ml.llm import generate_llm_response
    from backend.services.safety import detect_crisis, CRISIS_RESPONSE

except ImportError:
    from classifier import detect_emotion, detect_topic
    from memory import build_history
    from coping import coping_suggestions
    from llm import generate_llm_response
    from safety import detect_crisis, CRISIS_RESPONSE
st.set_page_config(
    page_title="Teen Mental Health Support Chatbot",
    page_icon="💬",
    layout="wide"
)

st.title("Teen Mental Health Support Chatbot 💬")

st.markdown("""
This chatbot is an AI support tool for teenagers dealing with:

• Family issues  
• Peer pressure  
• Career or exam stress  

⚠️ **This chatbot cannot replace a therapist or emergency help.**
""")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Share what you're going through...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Crisis detection
    if detect_crisis(user_input):

        reply = CRISIS_RESPONSE
        emotion = "crisis"
        topic = "safety"

    else:

        emotion = detect_emotion(user_input)
        topic = detect_topic(user_input)

        history_text = build_history(st.session_state.messages)

        suggestions = coping_suggestions(topic)

        prompt = f"""
You are a compassionate mental health support chatbot for teenagers.

Conversation history:
{history_text}

User message:
{user_input}

Detected emotion: {emotion}
Detected topic: {topic}

Helpful coping suggestions:
{suggestions}

Instructions:
- Respond empathetically
- Validate feelings
- Provide practical coping advice
- Avoid repeating phrases
- Ask one supportive follow-up question
"""

        reply = generate_llm_response(prompt)

    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })