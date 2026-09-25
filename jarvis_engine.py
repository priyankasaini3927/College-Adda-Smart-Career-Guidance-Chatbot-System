import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


SYSTEM_PROMPT = """
You are Jarvis, the AI career guidance assistant for College Adda.

College Adda helps 12th-grade science students understand:
- Engineering career options
- Engineering branches
- JEE and MHT-CET
- College and branch selection
- Skills required for different careers
- AI, Data Science, CSE, Mechanical, Electronics, Electrical and related fields
- College life and learning roadmaps

Your job is to give practical, student-friendly guidance.

Rules:
1. Keep answers clear and easy to understand.
2. Prefer practical advice over generic motivational statements.
3. Explain technical terms when necessary.
4. Do not invent college cutoffs, rankings, fees, placement numbers, or admission rules.
5. For current cutoff/admission information, clearly say that official counselling sources should be checked.
6. Do not guarantee admission, placement, salary, or career success.
7. When comparing engineering branches, explain differences in subjects, coding requirements, career paths, and skills.
8. When a student asks what they should choose, explain the factors they should consider instead of blindly deciding for them.
9. Focus on Indian engineering education, especially Maharashtra/JEE/MHT-CET context.
10. Keep the answer concise unless the student asks for a detailed explanation.
"""


def jarvis_answer(question: str) -> str:
    """Return a College Adda career-guidance response."""

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "GROQ_API_KEY is missing. Please check your .env file."

    if not question.strip():
        return "Please enter a question."

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": question.strip(),
                },
            ],
        )

        return response.choices[0].message.content

    except Exception as exc:
        return (
            "Sorry, Jarvis is temporarily unavailable.\n"
            f"Error: {exc}"
        )