import webbrowser
from urllib.parse import quote_plus

from jarvis_engine import jarvis_answer, jarvis_profile_analysis


def greet():
    print("\nWelcome to College Adda - Smart Career Guidance Bot")
    print("------------------------------------------------------")


def get_exam():
    while True:
        exam = input("Which entrance exam did you give? (JEE / MHT-CET): ").strip().lower()
        if "jee" in exam:
            return "JEE"
        if "mht" in exam or "cet" in exam:
            return "MHT-CET"
        print("Invalid exam. Please enter JEE or MHT-CET.")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid non-negative number.")


def jee_analysis():
    rank = get_int("Enter your JEE rank: ")
    marks = get_int("Enter your JEE marks: ")

    if marks >= 250 and rank <= 500:
        print("Excellent! You can target highly competitive options.")
    elif marks >= 180:
        print("You can target competitive options across NITs/IIITs and other institutes.")
    else:
        print("Consider a wider range of state, private, and other engineering options.")

    return {"rank": rank, "marks": marks}


def cet_analysis():
    rank = get_int("Enter your MHT-CET rank: ")
    marks = get_int("Enter your MHT-CET marks: ")

    if marks >= 150 and rank <= 1000:
        print("Excellent score!")
    elif marks >= 120 and rank <= 2000:
        print("Good score!")
    else:
        print("Consider a broader set of options.")

    return {"rank": rank, "marks": marks}


def interest_analysis():
    while True:
        interest = input(
            "\nWhat are you interested in? "
            "(coding/ai/robots/electrical/machinery): "
        ).strip().lower()

        if "coding" in interest or "cse" in interest:
            print("Suggested Branch: CSE")
            return {"interest": interest, "suggested_branch": "CSE"}
        if "ai" in interest or "data" in interest:
            print("Suggested Branch: AI & DS")
            return {"interest": interest, "suggested_branch": "AI & DS"}
        if "robot" in interest or "machine" in interest:
            print("Suggested Branch: Mechanical")
            return {"interest": interest, "suggested_branch": "Mechanical"}
        if "electrical" in interest or "electronics" in interest:
            print("Suggested Branch: Electronics")
            return {"interest": interest, "suggested_branch": "Electronics"}

        print("Please choose one of the listed interest areas.")


def career_goal():
    while True:
        goal = input(
            "\nWhat is your main career goal? "
            "(software/ai-data/robotics/core-engineering/other): "
        ).strip().lower()
        if goal:
            return goal
        print("Please enter your career goal.")


def preferred_location():
    location = input(
        "Preferred study location (e.g. Mumbai/Pune/anywhere in Maharashtra): "
    ).strip()
    return location or "Not specified"


def college_type():
    while True:
        ctype = input("\nWhich college type do you prefer? (government/private): ").strip().lower()

        if "government" in ctype:
            print("\nGovernment options shown by this demo:")
            print("1. COEP Pune\n2. VJTI Mumbai\n3. SPCE Mumbai\n4. Walchand Sangli\n5. GCOE Aurangabad")
            return "Government"

        if "private" in ctype:
            print("\nPrivate options shown by this demo:")
            print("1. VIT Pune\n2. MIT WPU\n3. PCCOE\n4. DY Patil\n5. Sinhgad")
            return "Private"

        print("Please enter Government or Private.")


def college_search():
    choice = input("\nDo you want to search a specific college? (yes/no): ").strip().lower()
    if choice.startswith("y"):
        name = input("Enter college name: ").strip()
        if name:
            webbrowser.open(
                f"https://www.google.com/search?q={quote_plus(name + ' engineering college')}"
            )
            print("Opening browser...")
            return name
    return None


def predict_colleges_branchwise(branch, marks):
    # Demo values from the original project. Verify current counselling data before
    # using these for real admission decisions.
    cutoffs = {
        "CSE": {
            "COEP Pune": 152,
            "VJTI Mumbai": 150,
            "SPIT Mumbai": 148,
            "VIT Pune": 140,
            "PCCOE Pune": 135,
        },
        "AI & DS": {
            "COEP Pune": 150,
            "VJTI Mumbai": 148,
            "SPIT Mumbai": 145,
            "VIT Pune": 138,
            "PCCOE Pune": 132,
        },
        "Mechanical": {
            "COEP Pune": 145,
            "VJTI Mumbai": 142,
            "Walchand Sangli": 135,
            "VIT Pune": 130,
            "PCCOE Pune": 125,
        },
        "Electronics": {
            "COEP Pune": 148,
            "VJTI Mumbai": 145,
            "SPIT Mumbai": 142,
            "VIT Pune": 135,
            "PCCOE Pune": 130,
        },
    }

    if branch not in cutoffs:
        print("Sorry, no project data is available for this branch yet.")
        return {"best_options": [], "safe_options": [], "backup_options": []}

    print(f"\nCollege Prediction for {branch} branch (demo data):\n")

    best = []
    safe = []
    backup = []

    for college, cutoff in cutoffs[branch].items():
        if marks >= cutoff + 5:
            best.append(college)
        elif marks >= cutoff:
            safe.append(college)
        elif marks >= cutoff - 5:
            backup.append(college)

    if best:
        print("Best Options:")
        for college in best:
            print("  -->", college)

    if safe:
        print("\nSafe Options:")
        for college in safe:
            print("  -->", college)

    if backup:
        print("\nBackup Options:")
        for college in backup:
            print("  -->", college)

    if not best and not safe and not backup:
        print("Your score is below the demo cutoffs for this branch.")

    return {
        "best_options": best,
        "safe_options": safe,
        "backup_options": backup,
    }


def show_profile(profile):
    print("\n" + "=" * 62)
    print("YOUR COLLEGE ADDA PROFILE")
    print("=" * 62)
    labels = [
        ("entrance_exam", "Entrance Exam"),
        ("marks", "Marks"),
        ("rank", "Rank"),
        ("interest", "Interest"),
        ("career_goal", "Career Goal"),
        ("suggested_branch", "Suggested Branch"),
        ("college_preference", "College Preference"),
        ("preferred_location", "Preferred Location"),
    ]
    for key, label in labels:
        value = profile.get(key)
        if value:
            print(f"{label:20}: {value}")
    print("=" * 62)


def personalized_jarvis_session(profile):
    """Automatically personalize Jarvis first, then continue with follow-up questions."""
    show_profile(profile)

    print("\n🤖 Jarvis is building your personalized career plan...\n")
    print(jarvis_profile_analysis(profile))

    print("\n" + "-" * 62)
    print("Ask Jarvis follow-up questions using THIS profile.")
    print("Type 'done' when you want to finish.")
    print("-" * 62)

    history = []

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in {"done", "exit", "quit"}:
            break
        if not question:
            continue

        answer = jarvis_answer(
            question,
            student_context=profile,
            conversation_history=history,
        )

        print(f"\n🤖 Jarvis: {answer}")

        history.append({"role": "user", "content": question})
        history.append({"role": "assistant", "content": answer})


def career_guidance():
    exam = get_exam()

    if exam == "JEE":
        exam_data = jee_analysis()
    else:
        exam_data = cet_analysis()

    interest_data = interest_analysis()
    goal = career_goal()
    location = preferred_location()
    branch = interest_data["suggested_branch"]

    recommendations = predict_colleges_branchwise(branch, exam_data["marks"])
    college_preference = college_type()
    searched_college = college_search()

    profile = {
        "entrance_exam": exam,
        "marks": exam_data["marks"],
        "rank": exam_data["rank"],
        "interest": interest_data["interest"],
        "career_goal": goal,
        "suggested_branch": branch,
        "college_preference": college_preference,
        "preferred_location": location,
        "best_options": ", ".join(recommendations["best_options"]),
        "safe_options": ", ".join(recommendations["safe_options"]),
        "backup_options": ", ".join(recommendations["backup_options"]),
    }

    if searched_college:
        profile["searched_college"] = searched_college

    personalized_jarvis_session(profile)


def main():
    greet()

    msg = input("Say Hi to start: ").strip().lower()
    if "hi" in msg or "hello" in msg:
        print("Hello! Let's plan your future 🚀")

    print("\nChoose an option:")
    print("1. Career Guidance + Personalized Jarvis")
    print("2. Ask Jarvis (General Question)")

    choice = input("Enter choice (1/2): ").strip()

    if choice == "2":
        question = input("\nAsk your question: ").strip()
        print("\n🤖 Jarvis is thinking...\n")
        print(jarvis_answer(question))
        return

    if choice == "1":
        career_guidance()
        print("\nThank you for using College Adda. All the best for your future!")
        return

    print("Invalid choice. Please run the program again and choose 1 or 2.")


if __name__ == "__main__":
    main()
