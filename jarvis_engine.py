import os
from typing import Any

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

SYSTEM_PROMPT = """
You are Jarvis, the AI career guidance assistant for College Adda.

College Adda helps Indian Class 12 science students understand engineering
career options, entrance exams, branches, skills, and college selection.

Use the student's profile as the primary personalization context. Never ignore
profile information when it is provided. Explicitly connect your advice to the
student's exam, marks, rank, interests, career goal, preferred college type,
preferred location, suggested branch, and available college options.

Rules:
1. Give practical, student-friendly guidance.
2. Explain WHY a recommendation fits the student's profile.
3. Do not invent cutoffs, fees, rankings, placements, admission rules, or
   other time-sensitive facts.
4. Treat any college lists/cutoffs supplied by College Adda as demo/project
   data unless verified by an official source.
5. For current admission/cutoff information, tell the student to verify the
   official counselling or college source.
6. Do not guarantee admission, placement, salary, or career success.
7. When comparing branches, explain subjects, coding intensity, skills,
   career paths, and trade-offs.
8. Do not make the final career decision for the student; give clear factors
   they can use to decide.
9. Keep answers concise by default, but be structured when useful.
""".strip()


def _build_context(student_context: dict[str, Any] | None) -> str:
    if not student_context:
        return "No student profile was provided. Answer as a general career assistant."

    lines = [
        "PERSONALIZED STUDENT PROFILE",
        "Use these details throughout the answer and connect advice directly to them.",
    ]

    for key, value in student_context.items():
        if value is None or str(value).strip() == "":
            continue
        label = key.replace("_", " ").title()
        lines.append(f"- {label}: {value}")

    return "\n".join(lines)


def _call_groq(messages: list[dict[str, str]]) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "GROQ_API_KEY is missing. Please check your .env file."

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
    )

    content = response.choices[0].message.content
    return content.strip() if content else "Jarvis did not return a response."


def jarvis_profile_analysis(student_context: dict[str, Any]) -> str:
    """Generate an automatic personalized career analysis from the collected profile."""
    prompt = f"""
{_build_context(student_context)}

Create a personalized College Adda career analysis using ONLY the information
provided above.

Return these sections:
1. Your Student Profile — summarize the actual inputs in 2-4 lines.
2. Why This Branch Fits — connect the student's interest and career goal to
   the suggested branch. Mention trade-offs where relevant.
3. College Strategy — discuss how the student's marks/rank and stated college
   preference should influence the college shortlist. If project/demo college
   options are provided, use them only as the available project options and
   explicitly say they must be verified against current official data.
4. Skill Roadmap — give 3-5 concrete skills the student should start building.
5. Next 30 Days — give a realistic week-by-week action plan.
6. One Thing to Watch Out For — identify one profile-specific risk or gap.

Do not invent missing information and do not claim that any admission outcome
is guaranteed.
""".strip()

    try:
        return _call_groq(
            [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ]
        )
    except Exception as exc:
        return f"Sorry, personalized Jarvis analysis is temporarily unavailable.\nError: {exc}"


def jarvis_answer(
    question: str,
    student_context: dict[str, Any] | None = None,
    conversation_history: list[dict[str, str]] | None = None,
) -> str:
    """Answer a question using the student's profile and optional session history."""
    question = question.strip()
    if not question:
        return "Please enter a question."

    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if conversation_history:
            messages.extend(conversation_history[-8:])

        messages.append(
            {
                "role": "user",
                "content": f"{_build_context(student_context)}\n\nStudent question:\n{question}",
            }
        )

        return _call_groq(messages)
    except Exception as exc:
        return f"Sorry, Jarvis is temporarily unavailable.\nError: {exc}"
