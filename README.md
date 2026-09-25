# College Adda – Smart Career Guidance Chatbot System

College Adda is a **Python-based career guidance chatbot for Class 12 science students**. It combines a rule-based student-profile workflow with a **Groq-powered Jarvis assistant** to provide branch, college-strategy, skill-roadmap, and career-guidance support.

The current version focuses on **JEE / MHT-CET**, engineering branches, student interests, career goals, college-type preferences, and a personalized Jarvis session.

> **Important:** College prediction values and college lists currently included in the program are **demo/project data**. They must be verified against current official counselling and college sources before being used for real admission decisions.

---

## ✨ Current Features

### 1. Student Profile Collection
The chatbot collects:

- Entrance exam: **JEE / MHT-CET**
- Marks
- Rank
- Interest area
- Career goal
- Suggested engineering branch
- Preferred college type
- Preferred study location
- Optional specific-college search

### 2. Rule-Based Branch Suggestion
The current prototype maps interests to branches using simple keyword rules such as:

- Coding / CSE → **CSE**
- AI / Data → **AI & DS**
- Robotics / Machinery → **Mechanical**
- Electrical / Electronics → **Electronics**

This part is **rule-based**, not a trained machine-learning model.

### 3. Branch-Wise College Prediction Demo
The project contains demo cutoff values for selected branches and colleges and groups options into:

- Best Options
- Safe Options
- Backup Options

These values are included for demonstrating the chatbot flow and are **not live admission data**.

### 4. Personalized Jarvis
After collecting the student profile, Jarvis automatically generates a personalized analysis using the student's actual inputs.

The analysis covers:

1. Student profile summary
2. Why the suggested branch may fit the profile
3. College-selection strategy
4. Recommended skills
5. A 30-day action plan
6. One profile-specific risk or gap

### 5. Context-Aware Follow-Up Questions
During the personalized Jarvis session, the student's profile remains available to the AI.

The session also keeps recent conversation history, allowing questions such as:

> "Should I consider CSE instead?"

without requiring the student to repeat their marks, rank, interests, and goals every time.

### 6. General Jarvis Mode
Students can also use Jarvis directly for general career questions without creating a profile first.

---

## 🧠 How the System Works

```text
User
  │
  ▼
main.py
  │
  ├── Exam & marks collection
  ├── Interest analysis
  ├── Career goal
  ├── College preference
  ├── Location
  └── Demo college prediction
          │
          ▼
   Student Profile
          │
          ▼
 personalized_jarvis_session()
          │
          ▼
   jarvis_engine.py
          │
          ├── Student profile context
          ├── Conversation history
          └── Career-guidance system prompt
          │
          ▼
       Groq API
          │
          ▼
     Jarvis Response
```

---

## 📁 Project Structure

```text
College-Adda-Smart-Career-Guidance-Chatbot-System/
│
├── main.py              # Main CLI application and student workflow
├── jarvis_engine.py     # Groq integration + personalized Jarvis logic
├── requirements.txt     # Python dependencies
├── .gitignore           # Prevents secrets and virtual environments from being committed
├── .env                 # Local API key file (create this yourself; do not commit)
└── README.md            # Project documentation
```

---

## ⚙️ Tech Stack

- **Python** – Core application
- **Groq API** – LLM backend for Jarvis
- **OpenAI GPT-OSS 20B on Groq** – Current model used by the project
- **python-dotenv** – Loads the API key from `.env`
- **Webbrowser / Google Search** – Optional specific-college search
- **CLI / Terminal UI** – Current user interface

---

## 🚀 Setup & Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd College-Adda-Smart-Career-Guidance-Chatbot-System
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Create `.env`

Create a file named `.env` in the project root:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Do **not** commit `.env` to GitHub.

### 5. Run the application

```powershell
python main.py
```

---

## 🖥️ Example Flow

```text
Welcome to College Adda - Smart Career Guidance Bot

Say Hi to start: hi

Choose an option:
1. Career Guidance + Personalized Jarvis
2. Ask Jarvis (General Question)

Enter choice (1/2): 1
```

The career-guidance flow then collects the student's profile and automatically starts the personalized Jarvis session.

Example question:

```text
Should I choose CSE or AI & DS based on my interests?
```

Jarvis receives the student's profile along with the question and uses both when generating the response.

---

## 🔐 Environment Variables & Security

The project expects:

```env
GROQ_API_KEY=...
```

Keep API keys out of source code and screenshots, and never commit them to Git.

The included `.gitignore` protects common local files:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

If an API key has already been exposed publicly, revoke/rotate it before continuing to use the repository.

---

## ⚠️ Current Limitations

1. **College cutoffs are static demo values.** They are not fetched live.
2. **College lists are limited to the project's current demo dataset.**
3. **Branch suggestion is keyword/rule based**, not ML based.
4. The chatbot currently runs in the **terminal**, not as a web application.
5. Jarvis can provide guidance, but it does not guarantee admission, placement, salary, or any specific career outcome.
6. Current admission information should always be verified using official counselling and college sources.

---

## 🔮 Planned Upgrades

- Live counselling / cutoff data integration
- College database with structured filters
- Better branch recommendation logic
- User accounts and saved profiles
- Web UI using Flask or FastAPI + frontend
- Persistent chat history
- More engineering branches and career paths
- Explainable recommendation scoring
- Official-source links for admission information

---

## 🧪 Development Notes

The current architecture deliberately keeps the **student workflow and rules in `main.py`** and the **LLM functionality in `jarvis_engine.py`**.

This separation makes it easier to replace the model provider, add a web interface, or add a database layer later without rewriting the complete application.

---

## 👩‍💻 Author

**Priyanka Saini**  
B.Tech – Artificial Intelligence & Data Science

---

## 📌 Project Status

**Current status:** Working CLI prototype with Groq-powered personalized Jarvis integration.
