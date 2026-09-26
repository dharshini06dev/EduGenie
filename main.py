import os
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(
    title="EduGenie - AI Powered Learning Assistant",
    description="Full-stack AI educational assistant powered by Google Gemini (Naan Mudhalvan / IBM SkillsBuild Project)",
    version="2.0.0"
)

# Ensure static directories exist
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Pydantic Schemas for API clients
class QueryRequest(BaseModel):
    query: str
    language: str = "English"

class QuizRequest(BaseModel):
    topic: str
    language: str = "English"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Loads the EduGenie unified dashboard"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/qa")
async def handle_qa(request: Request, query: str = Form(None), language: str = Form("English")):
    """Handles Academic & General Q&A"""
    # Support both JSON body and Form data
    if not query:
        try:
            body = await request.json()
            query = body.get("query", "")
            language = body.get("language", "English")
        except Exception:
            pass

    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")
        
    answer = answer_question(query, language=language)
    return JSONResponse(content={"status": "success", "type": "qa", "query": query, "result": answer})

@app.post("/explain")
async def handle_explain(request: Request, query: str = Form(None), language: str = Form("English")):
    """Handles Simplified Concept Explanations"""
    if not query:
        try:
            body = await request.json()
            query = body.get("query", "")
            language = body.get("language", "English")
        except Exception:
            pass

    if not query:
        raise HTTPException(status_code=400, detail="Topic or concept is required")
        
    explanation = explain_concept(query, language=language)
    return JSONResponse(content={"status": "success", "type": "explain", "topic": query, "result": explanation})

@app.post("/quiz")
async def handle_quiz(request: Request, topic: str = Form(None), language: str = Form("English")):
    """Generates 3 interactive MCQs from passage or topic"""
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

@app.post("/summarize")
async def handle_summarize(request: Request, query: str = Form(None), language: str = Form("English")):
    """Condenses long educational passages"""
    if not query:
        try:
            body = await request.json()
            query = body.get("query", "") or body.get("passage", "")
            language = body.get("language", "English")
        except Exception:
            pass

    if not query:
        raise HTTPException(status_code=400, detail="Passage is required")
        
    summary = summarize_text(query, language=language)
    return JSONResponse(content={"status": "success", "type": "summarize", "result": summary})

@app.post("/learn/recommendations")
async def handle_learning_path(request: Request, topic: str = Form(None), language: str = Form("English")):
    """Provides structured learning roadmaps"""
    if not topic:
        try:
            body = await request.json()
            topic = body.get("topic", "") or body.get("query", "")
            language = body.get("language", "English")
        except Exception:
            pass

    if not topic:
        raise HTTPException(status_code=400, detail="Topic is required")
        
    roadmap = get_learning_recommendations(topic, language=language)
    return JSONResponse(content={"status": "success", "type": "learning_path", "topic": topic, "result": roadmap})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
