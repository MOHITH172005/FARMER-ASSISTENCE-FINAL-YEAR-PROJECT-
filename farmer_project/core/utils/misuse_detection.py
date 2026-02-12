def detect_misuse(message):
    msg = message.lower()

    # 🔴 HIGH-RISK → BLOCK
    high_risk = [
        "kill", "murder", "suicide", "rape",
        "terrorist", "bomb", "sex with child"
    ]

    # 🟡 LOW-RISK → WARNING ONLY
    mild_profanity = [
        "fuck", "shit", "bitch", "asshole"
    ]

    for word in high_risk:
        if word in msg:
            return "dangerous_content", 0.95

    for word in mild_profanity:
        if word in msg:
            return "profanity", 0.40

    return None, 0.0
