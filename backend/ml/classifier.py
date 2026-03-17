from transformers import pipeline

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

def detect_emotion(text):

    result = emotion_model(text)[0][0]

    return result["label"]


CAREER_WORDS = ["placement","job","interview","career","company","offer"]
STUDY_WORDS = ["exam","study","assignment","college","marks","grades"]
FAMILY_WORDS = ["parents","family","mom","dad","argue","fight"]
PEER_WORDS = ["friends","bullying","peer pressure","classmates"]
CONFIDENCE_WORDS = ["confidence","self doubt","failure","not good enough"]


def detect_topic(text):

    text = text.lower()

    if any(w in text for w in CAREER_WORDS):
        return "career"

    elif any(w in text for w in STUDY_WORDS):
        return "study"

    elif any(w in text for w in FAMILY_WORDS):
        return "family"

    elif any(w in text for w in PEER_WORDS):
        return "peer"

    elif any(w in text for w in CONFIDENCE_WORDS):
        return "confidence"

    return "general"