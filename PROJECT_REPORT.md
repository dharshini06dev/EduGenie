# IBM SkillsBuild / Naan Mudhalvan Internship Project Report
## PROJECT REPORT ON:
# **EduGenie: Google Gemini Powered Learning Assistant**

---

### **Project & Student Details**
- **Project Title:** EduGenie: Google Gemini Powered Learning Assistant
- **Domain:** Artificial Intelligence, Generative AI & Cloud Services
- **Program:** Naan Mudhalvan - IBM SkillsBuild Emerging Technologies Program
- **Student / Team Lead:** Priya Dharshini & Team
- **Academic Year:** 2025–2026
- **Technologies Used:** Python 3.12, FastAPI, Google Gemini Models, Jinja2, HTML5/CSS3, RESTful APIs, Uvicorn

---

## **TABLE OF CONTENTS**
1. [Abstract / Executive Summary](#1-abstract--executive-summary)
2. [Introduction & Background](#2-introduction--background)
3. [Problem Statement & Objectives](#3-problem-statement--objectives)
4. [System Requirements](#4-system-requirements)
5. [System Architecture & Workflow](#5-system-architecture--workflow)
6. [Detailed Module Design & REST API Specifications](#6-detailed-module-design--rest-api-specifications)
7. [Source Code Implementation](#7-source-code-implementation)
8. [Testing, Test Cases & Output Snapshots](#8-testing-test-cases--output-snapshots)
9. [Installation & Deployment Guide](#9-installation--deployment-guide)
10. [Conclusion & Future Scope](#10-conclusion--future-scope)

---

## **1. Abstract / Executive Summary**
In the contemporary digital era, personalized education is pivotal for students preparing for academic and technical excellence. **EduGenie** is a next-generation interactive AI Learning Companion engineered on an asynchronous FastAPI framework and powered by Google Gemini Large Language Models (LLMs). 

The platform integrates five core academic workflows into a unified, responsive interface:
1. **Academic & General Q&A:** High-accuracy question answering with structured facts.
2. **Simplified Concept Breakdown:** Deep conceptual explanations enhanced with real-world analogies and key takeaways.
3. **Interactive 3-MCQ Quiz Generator:** Passage and topic-based multiple-choice question generation with instant evaluation and feedback.
4. **Passage Summarizer:** High-speed executive summaries and bullet points from long study material.
5. **Personalized Learning Path:** Step-by-step roadmap from Beginner to Advanced levels with curated learning resources.

---

## **2. Introduction & Background**
Traditional educational workflows are often fragmented across multiple disconnected websites and tools. Students struggle to break down complex theoretical concepts into understandable everyday analogies or get instant, customized assessments on specific notes.

EduGenie addresses these challenges by consolidating Generative AI capabilities into a streamlined, corporate-grade dashboard. With full mobile responsiveness and light/dark theme adaptation, EduGenie democratizes access to intelligent tutoring.

---

## **3. Problem Statement & Objectives**

### **3.1 Problem Statement**
- Rote memorization often replaces conceptual comprehension in standard curricula.
- Lack of immediate automated quiz evaluation aligned specifically with newly learned topics.
- Difficulty in formulating realistic, stage-by-stage learning roadmaps for new technical domains.

### **3.2 Key Objectives**
- Develop an asynchronous, high-throughput REST API using FastAPI.
- Implement multi-model rotation across Google Gemini LLMs with real-time failover.
- Provide a clean Single Page Application (SPA) dashboard with responsive CSS and zero external heavy JS dependencies.
- Enable instant client-side quiz interaction with color-coded answer validation.

---

## **4. System Requirements**

### **4.1 Hardware Requirements**
- **Processor:** Intel Core i3 / AMD Ryzen 3 or higher
- **RAM:** Minimum 4 GB (8 GB recommended)
- **Disk Space:** 500 MB free space
- **Network:** Active internet connection for Google Gemini & Cloud API endpoints

### **4.2 Software Requirements**
- **Operating System:** Windows 10/11, macOS, or Linux (Ubuntu 20.04+)
- **Programming Language:** Python 3.10 to 3.12
- **Frameworks & Libraries:**
  - `fastapi` & `uvicorn[standard]`
  - `google-generativeai`
  - `python-dotenv`
  - `jinja2`
  - `requests` & `urllib3`
- **Web Browser:** Google Chrome, Microsoft Edge, Firefox, or Safari

---

## **5. System Architecture & Workflow**

### **5.1 High-Level Architecture Diagram**

```
+-------------------------------------------------------------------------+
|                         CLIENT LAYER (BROWSER)                          |
|  - Unified Single-Page Interface (templates/index.html)                 |
|  - Modern Corporate Design System & Dark/Light Theme (static/style.css) |
|  - Interactive JS Async Fetch & Instant Card Evaluation                 |
+-------------------------------------------------------------------------+
                                    │
                                    │ HTTP / RESTful Requests (JSON / Form)
                                    ▼
+-------------------------------------------------------------------------+
|                       APPLICATION SERVER LAYER                          |
|                       FastAPI & Uvicorn (main.py)                       |
|   ├── GET  /                   -> Web Dashboard                         |
|   ├── POST /qa                 -> Academic Q&A Engine                   |
|   ├── POST /explain            -> Concept Simplifier Engine             |
|   ├── POST /quiz               -> 3-MCQ Generator Engine                |
|   ├── POST /summarize          -> Study Notes Summarizer                |
|   └── POST /learn/recommendations -> Roadmap Engine                     |
+-------------------------------------------------------------------------+
                                    │
                                    ▼
+-------------------------------------------------------------------------+
|                         BUSINESS LOGIC LAYER                            |
|  - qna.py                - explanation_module.py                        |
|  - quiz_module.py        - summary_module.py                            |
|  - learning_path.py                                                     |
+-------------------------------------------------------------------------+
                                    │
                                    ▼
+-------------------------------------------------------------------------+
|                  AI ORCHESTRATION & RESILIENCE ENGINE                   |
|                        (gemini_helper.py)                               |
|  - Google Gemini 1.5 Flash / Pro Rotation                               |
|  - Real-Time Live AI Fallback & Dynamic Knowledge Synthesis Engine      |
+-------------------------------------------------------------------------+
```

---

## **6. Detailed Module Design & REST API Specifications**

| # | Endpoint | Method | Request Payload | Response Schema | Description |
|---|---|---|---|---|---|
| 1 | `/` | `GET` | None | `HTMLResponse` | Renders the unified interactive dashboard |
| 2 | `/qa` | `POST` | `{"query": "...", "language": "English"}` | `{"status": "success", "result": "..."}` | Answers academic queries with facts & bullets |
| 3 | `/explain` | `POST` | `{"query": "...", "language": "English"}` | `{"status": "success", "result": "..."}` | Explains concepts with real-world analogies |
| 4 | `/quiz` | `POST` | `{"topic": "...", "language": "English"}` | `{"status": "success", "quizzes": [...]}` | Produces 3 MCQs with 4 options & answer key |
| 5 | `/summarize` | `POST` | `{"query": "...", "language": "English"}` | `{"status": "success", "result": "..."}` | Summarizes long texts with key takeaways |
| 6 | `/learn/recommendations` | `POST` | `{"topic": "...", "language": "English"}` | `{"status": "success", "result": "..."}` | Generates 3-Level Beginner to Advanced roadmap |

---

## **7. Source Code Implementation**

### **7.1 Server Gateway (`main.py`)**
```python
import os
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(
    title="EduGenie - AI Powered Learning Assistant",
    description="Full-stack AI educational assistant powered by Google Gemini",
    version="2.0.0"
)

STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/qa")
async def handle_qa(request: Request, query: str = Form(None), language: str = Form("English")):
    if not query:
        try:
            body = await request.json()
            query = body.get("query", "")
            language = body.get("language", "English")
        except Exception:
            pass
    if not query:
        raise HTTPException(status_code=400, detail="Query is required")
    answer = answer_question(query, language=language)
    return JSONResponse(content={"status": "success", "type": "qa", "query": query, "result": answer})

@app.post("/quiz")
async def handle_quiz(request: Request, topic: str = Form(None), language: str = Form("English")):
    if not topic:
        try:
            body = await request.json()
            topic = body.get("topic", "") or body.get("query", "")
            language = body.get("language", "English")
        except Exception:
            pass
    if not topic:
        raise HTTPException(status_code=400, detail="Topic or passage is required")
    quizzes = generate_quiz(topic, language=language)
    return JSONResponse(content={"status": "success", "type": "quiz", "topic": topic, "quizzes": quizzes})
```

---

### **7.2 Resilient Multi-Tier AI Helper (`gemini_helper.py`)**
```python
import os
import requests
import urllib3
import google.generativeai as genai
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

GEMINI_MODELS = [
    "gemini-1.5-flash",
    "gemini-1.5-pro",
    "gemini-2.0-flash-exp",
    "gemini-flash-latest",
    "gemini-pro-latest"
]

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if api_key:
        genai.configure(api_key=api_key)
        return True
    return False

def generate_text_with_rotation(prompt: str, system_instruction: str = "") -> str:
    full_prompt = f"{system_instruction}\n\n{prompt}" if system_instruction else prompt

    # 1. Primary: Google Gemini Rotation Chain
    if get_gemini_client():
        for model_name in GEMINI_MODELS:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(full_prompt)
                if response and response.text:
                    return response.text.strip()
            except Exception:
                continue

    # 2. Secondary: Real-time Live Fallback & Knowledge Synthesis
    try:
        import urllib.parse
        encoded = urllib.parse.quote(full_prompt)
        res = requests.get(f"https://text.pollinations.ai/{encoded}", verify=False, timeout=10)
        if res.status_code == 200 and len(res.text.strip()) > 5:
            return res.text.strip()
    except Exception:
        pass

    return ""
```

---

### **7.3 3-MCQ Quiz Generator & Regex Parser (`quiz_module.py`)**
```python
import json
import re
from gemini_helper import generate_text_with_rotation

def clean_json_block(text: str) -> str:
    cleaned = re.sub(r"^```(?:json)?\s*", "", text.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    match = re.search(r'(\[.*\]|\{.*\})', cleaned, re.DOTALL)
    if match:
        return match.group(0).strip()
    return cleaned.strip()

def generate_quiz(topic_or_passage: str, language: str = "English") -> list:
    sys_prompt = f"""
    You are an AI Assessment Specialist in EduGenie.
    Generate exactly 3 high-quality MCQs for '{topic_or_passage}' in valid JSON.
    """
    raw_response = generate_text_with_rotation(topic_or_passage, sys_prompt)
    if raw_response:
        try:
            parsed = json.loads(clean_json_block(raw_response))
            if isinstance(parsed, dict):
                parsed = parsed.get("mcqs") or parsed.get("questions") or [parsed]
            if isinstance(parsed, list) and len(parsed) >= 1:
                return parsed[:3]
        except Exception:
            pass
    return []
```

---

## **8. Testing, Test Cases & Output Snapshots**

### **8.1 Test Case Matrix**

| Test Case ID | Module Tested | Input Provided | Expected Output | Status |
|---|---|---|---|---|
| **TC-01** | Q&A Engine | *"Why is the sky blue?"* | Rayleigh scattering explanation with bullet points | **PASSED** |
| **TC-02** | Concept Simplifier | *"Photosynthesis"* | Definition, sunlight-kitchen analogy, takeaways | **PASSED** |
| **TC-03** | Quiz Generator | *"Human Heart & Blood"* | 3 MCQs with options (A,B,C,D), correct answer, and explanation | **PASSED** |
| **TC-04** | Summarizer | Multi-paragraph passage on AI | 3-sentence executive summary & bullet points | **PASSED** |
| **TC-05** | Learning Roadmap | *"Full Stack Web Dev"* | Level 1 (Beginner), Level 2 (Intermediate), Level 3 (Advanced) | **PASSED** |
| **TC-06** | Theme Switcher | Click Theme Toggle Button | Changes CSS theme variables and saves to `localStorage` | **PASSED** |

---

### **8.2 Sample Output Snapshots**

#### **1. Academic Q&A Output (`POST /qa`)**
> **Input:** *"Why is the sky blue?"*  
> **Output:**
> - **Direct Answer:** The sky appears blue because molecules in Earth's atmosphere scatter sunlight in all directions. Blue light travels in smaller, shorter waves, so it scatters more than other colors (Rayleigh Scattering).
> - **Key Highlights:**
>   - Sunlight contains all colors of the rainbow.
>   - Violet and blue have the shortest wavelengths.
>   - Human eyes are more sensitive to blue light than violet.

#### **2. Interactive 3-MCQ Output (`POST /quiz`)**
```json
[
  {
    "id": 1,
    "question": "What is the primary role of the sinoatrial (SA) node in the heart?",
    "options": [
      "A) Regulate blood pressure",
      "B) Initiate electrical impulses that set heart rate",
      "C) Combine oxygenated and deoxygenated blood",
      "D) Filter waste from the bloodstream"
    ],
    "correct_answer": "B",
    "explanation": "The SA node is the natural pacemaker of the heart."
  },
  {
    "id": 2,
    "question": "Which valve prevents backflow into the left atrium?",
    "options": [
      "A) Tricuspid valve",
      "B) Pulmonary valve",
      "C) Mitral valve",
      "D) Aortic valve"
    ],
    "correct_answer": "C",
    "explanation": "The mitral (bicuspid) valve separates the left atrium and left ventricle."
  },
  {
    "id": 3,
    "question": "Which blood vessels supply oxygen to heart muscles?",
    "options": [
      "A) Carotid arteries",
      "B) Coronary arteries",
      "C) Pulmonary veins",
      "D) Renal arteries"
    ],
    "correct_answer": "B",
    "explanation": "Coronary arteries branch off the aorta to supply the myocardium."
  }
]
```

---

## **9. Installation & Deployment Guide**

### **9.1 Prerequisites**
1. Install Python 3.10+ from python.org.
2. Install Git from git-scm.com.

### **9.2 Execution Steps**
```bash
# 1. Clone repository
git clone https://github.com/your-username/EduGenie.git
cd EduGenie

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file with your Gemini key
echo GEMINI_API_KEY=your_gemini_api_key_here > .env

# 4. Run application
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
- Open `http://127.0.0.1:8000` to interact with the web dashboard.
- Open `http://127.0.0.1:8000/docs` to test APIs via Swagger UI.

---

## **10. Conclusion & Future Scope**

### **10.1 Conclusion**
EduGenie successfully fulfills all project requirements outlined by the **Naan Mudhalvan / IBM SkillsBuild Program**. By combining FastAPI's performance with multi-tier Generative AI resilience, EduGenie offers a fast, reliable, and accessible educational platform.

### **10.2 Future Scope**
- **Voice Assistant Integration:** Adding speech-to-text and text-to-speech for hands-free learning.
- **Document & PDF Uploads:** Automated extraction and flashcard generation from textbooks.
- **Adaptive Spaced Repetition:** Smart revision schedules tailored to individual student performance.

---
**Prepared & Submitted by:** Priya Dharshini & Team  
**Program:** Naan Mudhalvan / IBM SkillsBuild
