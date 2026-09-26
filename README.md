# 🧞‍♂️ EduGenie: Google Gemini Powered Learning Assistant

An AI-powered educational assistant developed for the **Naan Mudhalvan / IBM SkillsBuild Program**.

---

## 👥 Project Team & Submission Details
- **Project Title:** EduGenie: Google Gemini Powered Learning Assistant
- **Developed By:** Priya Dharshini and Team
- **Program:** Naan Mudhalvan / IBM SkillsBuild
- **Tech Stack:** FastAPI, Google Gemini Models, Jinja2, HTML5/CSS3, Uvicorn

---

## 🚀 Core Features & RESTful Endpoints

| Module | Endpoint | Description |
| :--- | :--- | :--- |
| **QnA Engine** | `POST /qa` | High-precision academic and general knowledge Q&A. |
| **Concept Explanation** | `POST /explain` | Simplifies complex topics for beginners and students. |
| **Quiz Generator** | `POST /quiz` | Generates 3 interactive MCQs with 4 options & instant answer validation. |
| **Summarizer** | `POST /summarize` | Condenses lengthy educational passages and notes. |
| **Learning Path** | `POST /learn/recommendations` | Structured roadmap (Beginner ➡️ Intermediate ➡️ Advanced) with resources. |

---

## 📁 Project Architecture
```text
EduGenie/
├── main.py                  # FastAPI server with all endpoints (/, /qa, /explain, /quiz, /summarize, /learn/recommendations)
├── explanation_module.py    # Concept explanation logic
├── qna.py                   # Question answering logic
├── quiz_module.py           # 3 MCQ quiz generator with clean_json_block
├── summary_module.py        # Educational text summarization logic
├── learning_path.py         # Step-by-step learning roadmap recommendations
├── gemini_helper.py         # Multi-model rotation & failover engine
├── templates/
│   └── index.html           # Interactive single-page dashboard
├── static/
│   └── style.css            # Modern responsive stylesheet
├── .env                     # GEMINI_API_KEY
├── requirements.txt         # Dependencies
├── run.bat                  # 1-Click launcher on Windows
└── README.md
```

---

## ⚡ How to Run Locally

### 1. Configure API Key in `.env`
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 2. Start Application
Double-click `run.bat` OR run in terminal:
```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 3. Open in Browser
- **Web App:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **API Documentation (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
