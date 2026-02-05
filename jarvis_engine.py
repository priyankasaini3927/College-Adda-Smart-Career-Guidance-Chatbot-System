def jarvis_answer(question):
    q = question.lower()

    if "after 12th science" in q:
        return (
            "After 12th science, students can choose Engineering, Medical, "
            "Pure Sciences, Research, or emerging fields like AI and Data Science. "
            "The decision should depend on interest and entrance exam score."
        )

    elif "engineering branches" in q or "branches" in q:
        return (
            "Popular engineering branches include CSE, AI & DS, Mechanical, "
            "Electrical, and Electronics. Coding-oriented students usually prefer CSE or AI."
        )

    elif "career" in q:
        return (
            "Career selection should be based on interest, aptitude, "
            "exam performance, and long-term goals."
        )

    elif "college" in q:
        return (
            "Choosing a college depends on branch cutoff, location, "
            "college reputation, and placement records."
        )

    else:
        return (
            "I am a basic career guidance bot. "
            "Please ask questions related to careers, exams, or engineering branches."
        )
