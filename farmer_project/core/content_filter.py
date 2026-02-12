VIOLENT_WORDS = ["kill", "attack", "bomb", "murder"]
SEXUAL_WORDS = ["sex", "nude", "porn", "xxx"]
ABUSE_WORDS = ["idiot", "hate", "stupid"]

def detect_misuse(text):
    text = text.lower()

    for word in VIOLENT_WORDS:
        if word in text:
            return "violence", 0.95

    for word in SEXUAL_WORDS:
        if word in text:
            return "sexual", 0.95

    for word in ABUSE_WORDS:
        if word in text:
            return "abuse", 0.90

    return None, 0.0
