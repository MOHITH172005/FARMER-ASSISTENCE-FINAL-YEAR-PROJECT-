from groq import Groq
from django.conf import settings

# 🔑 Initialize Groq client
client = Groq(api_key=settings.GROQ_API_KEY)


def ask_farming_ai(question):
    """
    Core function that sends the prompt to Groq AI
    and returns the response text.
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert agriculture assistant for Indian farmers.\n\n"
                    "VERY IMPORTANT RULES:\n"
                    "1. DO NOT use markdown symbols like **, ##, -, or : at the end of headings.\n"
                    "2. Use BIG emoji-based headings.\n"
                    "3. Leave one empty line between sections.\n"
                    "4. Use simple bullet points using • symbol only.\n\n"
                    "FORMAT EXACTLY LIKE THIS:\n\n"
                    "🌱 SOIL\n"
                    "• point\n"
                    "• point\n\n"
                    "🌤 CLIMATE\n"
                    "• point\n\n"
                    "🌾 FERTILIZER\n"
                    "• point\n\n"
                    "✅ TIPS\n"
                    "• point\n\n"
                    "Keep language very simple and farmer-friendly."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0.3,
        max_tokens=700
    )

    return completion.choices[0].message.content


def groq_chat(message):
    """
    Wrapper function used by views.py.
    This keeps imports clean and avoids ImportError.
    """

    return ask_farming_ai(message)
