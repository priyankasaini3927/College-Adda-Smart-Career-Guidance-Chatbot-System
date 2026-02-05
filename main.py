import webbrowser
from jarvis_engine import jarvis_answer

def greet():
    print("\nWelcome to College Adda - Smart Career Guidance Bot")
    print("------------------------------------------------------")

def get_exam():
    exam = input("Which entrance exam did you give? (JEE / MHT-CET): ").lower()
    if "jee" in exam:
        return "jee"
    elif "mht" in exam or "cet" in exam:
        return "mht-cet"
    else:
        print("Invalid exam. Please enter JEE or MHT-CET.")
        return get_exam()

def jee_analysis():
    rank = int(input("Enter your JEE rank: "))
    marks = int(input("Enter your JEE marks: "))

    if marks >= 250 and rank <= 500:
        print("Excellent! You can target IITs / Top NITs.")
    elif marks >= 180:
        print("You can get good NITs / IIITs.")
    else:
        print("You should focus on state or private universities.")
        
    return marks

def cet_analysis():
    rank = int(input("Enter your MHT-CET rank: "))
    marks = int(input("Enter your MHT-CET marks: "))

    if marks >= 150 and rank <= 1000:
        print("Excellent score!")
    elif marks >= 120 and rank <= 2000:
        print("Good score!")
    else:
        print("Average score!")

    return marks

def interest_analysis():
    interest = input("\nWhat are you interested in? (coding/ai/robots/electrical/machinery): ").lower()

    if "coding" in interest or "cse" in interest:
        print("Suggested Branch: CSE")
        return "cse"
    elif "ai" in interest or "data" in interest:
        print("Suggested Branch: AI & DS")
        return "ai"
    elif "robot" in interest or "machine" in interest:
        print("Suggested Branch: Mechanical")
        return "mechanical"
    elif "electrical" in interest or "electronics" in interest:
        print("Suggested Branch: Electronics")
        return "electronics"
    else:
        print("General branch selected.")
        return "cse"

def college_search():
    choice = input("\nDo you want to search a specific college? (yes/no): ").lower()
    if "yes" in choice:
        name = input("Enter college name: ")
        webbrowser.open(f"https://www.google.com/search?q={name}+engineering+college")
        print("Opening browser...")

def college_type():
    ctype = input("\nWhich college type do you prefer? (government/private): ").lower()

    if "government" in ctype:
        print("\nTop Government Colleges in Maharashtra:")
        print("1. COEP Pune\n2. VJTI Mumbai\n3. SPCE Mumbai\n4. Walchand Sangli\n5. GCOE Aurangabad")
    else:
        print("\nTop Private Colleges in Maharashtra:")
        print("1. VIT Pune\n2. MIT WPU\n3. PCCOE\n4. DY Patil\n5. Sinhgad")
        
def predict_colleges_branchwise(branch, marks):
    cutoffs = {
        "cse": {
            "COEP Pune": 152,
            "VJTI Mumbai": 150,
            "SPIT Mumbai": 148,
            "VIT Pune": 140,
            "PCCOE Pune": 135
        },
        "ai": {
            "COEP Pune": 150,
            "VJTI Mumbai": 148,
            "SPIT Mumbai": 145,
            "VIT Pune": 138,
            "PCCOE Pune": 132
        },
        "mechanical": {
            "COEP Pune": 145,
            "VJTI Mumbai": 142,
            "Walchand Sangli": 135,
            "VIT Pune": 130,
            "PCCOE Pune": 125
        },
        "electronics": {
            "COEP Pune": 148,
            "VJTI Mumbai": 145,
            "SPIT Mumbai": 142,
            "VIT Pune": 135,
            "PCCOE Pune": 130
        }
    }

    if branch not in cutoffs:
        print("Sorry, no data available for this branch yet.")
        return

    print(f"\nCollege Prediction for {branch.upper()} branch:\n")

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
        for c in best:
            print("  -->", c)

    if safe:
        print("\nSafe Options:")
        for c in safe:
            print("  -->", c)

    if backup:
        print("\nBackup Options:")
        for c in backup:
            print("  -->", c)

    if not best and not safe and not backup:
        print("Your score is below cutoffs for this branch.")

def main():
    greet()

    msg = input("Say Hi to start: ").lower()
    if "hi" in msg or "hello" in msg:
        print("Hello! Let's plan your future 🚀")
    
    print("Choose an option:")    
    print("1. Career Guidance")
    print("2. Ask Jarvis (General Question)")

    choice = input("Enter choice (1/2): ")

    if choice == "2":
        question = input("\nAsk your question: ")
        print("\n🤖 Jarvis is thinking...\n")
        print(jarvis_answer(question))
        return

    exam = get_exam()

    if exam == "jee":
        marks = jee_analysis()
    else:
        marks = cet_analysis()

    branch = interest_analysis()

    predict_colleges_branchwise(branch, marks)

    college_type()
    college_search()

    print("\nThank you for using College Adda. All the best for your future!")


main()
