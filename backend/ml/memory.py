def build_history(history):

    history_text = ""

    if history:

        for msg in history[-6:]:

            role = "User" if msg["role"] == "user" else "Assistant"

            history_text += f"{role}: {msg['content']}\n"

    return history_text