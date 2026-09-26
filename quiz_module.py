import os
import json
import re
from gemini_helper import generate_text_with_rotation

def clean_json_block(text: str) -> str:
    """Extracts valid JSON array or object from raw model text"""
    if not text:
        return ""
    # Strip markdown block wrappers
    cleaned = re.sub(r"^```(?:json)?\s*", "", text.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    
    # Try finding json array [...] or object {...}
    match = re.search(r'(\[.*\]|\{.*\})', cleaned, re.DOTALL)
    if match:
        return match.group(0).strip()
    return cleaned.strip()

def generate_quiz(topic_or_passage: str, language: str = "English") -> list:
    """
    Generates exactly 3 Multiple-Choice Questions (MCQs) from a passage or topic.
    Each MCQ has 4 options and the correct answer.
    """
    sys_prompt = f"""
    You are an AI Assessment Specialist in EduGenie.
    Generate exactly 3 high-quality Multiple-Choice Questions (MCQs) based on the topic or passage provided: '{topic_or_passage}'.
    
    Target Language: {language} (Options: English, Thanglish, or Tamil).
    
    CRITICAL: Output ONLY a valid JSON Array with exactly 3 objects. No conversational text.
    JSON Format:
    [
      {{
        "id": 1,
        "question": "Question 1 text here?",
        "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
        "correct_answer": "A",
        "explanation": "Brief explanation"
      }},
      {{
        "id": 2,
        "question": "Question 2 text here?",
        "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
        "correct_answer": "B",
        "explanation": "Brief explanation"
      }},
      {{
        "id": 3,
        "question": "Question 3 text here?",
        "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
        "correct_answer": "C",
        "explanation": "Brief explanation"
      }}
    ]
    """
    
    raw_response = generate_text_with_rotation(topic_or_passage, sys_prompt)
    if raw_response:
        try:
            cleaned = clean_json_block(raw_response)
            parsed = json.loads(cleaned)
            if isinstance(parsed, dict):
                # Wrapped in a dict or single question
                if "mcqs" in parsed and isinstance(parsed["mcqs"], list):
                    parsed = parsed["mcqs"]
                elif "questions" in parsed and isinstance(parsed["questions"], list):
                    parsed = parsed["questions"]
                elif "quizzes" in parsed and isinstance(parsed["quizzes"], list):
                    parsed = parsed["quizzes"]
                else:
                    parsed = [parsed]
                    
            if isinstance(parsed, list) and len(parsed) >= 1:
                # Normalize keys
                normalized = []
                for idx, item in enumerate(parsed[:3], 1):
                    q_text = item.get("question", f"Question {idx}")
                    opts = item.get("options") or item.get("choices") or []
                    if len(opts) < 4:
                        opts = [f"A) {opts[0] if len(opts)>0 else 'True'}", f"B) {opts[1] if len(opts)>1 else 'False'}", "C) Both A and B", "D) None of the above"]
                    
                    c_ans = item.get("correct_answer") or item.get("answer") or "A"
                    if isinstance(c_ans, int) and 0 <= c_ans < 4:
                        c_ans = ["A", "B", "C", "D"][c_ans]
                    elif str(c_ans).strip().upper() not in ["A", "B", "C", "D"]:
                        c_ans = str(c_ans).strip()[:1].upper() if str(c_ans).strip()[:1].upper() in ["A", "B", "C", "D"] else "A"
                    
                    expl = item.get("explanation") or "Accurate answer based on conceptual definitions."
                    normalized.append({
                        "id": idx,
                        "question": q_text,
                        "options": [f"{['A', 'B', 'C', 'D'][i]}) {opt.split(') ', 1)[-1] if ')' in str(opt) else str(opt)}" for i, opt in enumerate(opts[:4])],
                        "correct_answer": c_ans,
                        "explanation": expl
                    })
                return normalized
        except Exception as e:
            print(f"[Quiz Module] JSON parse error: {e}")

    # Smart Fallback Quizzes
    t_lower = topic_or_passage.lower()
    if "pythagoras" in t_lower:
        return [
            {
                "id": 1,
                "question": "What is the formula for the Pythagoras Theorem in a right-angled triangle?",
                "options": ["A) a² + b² = c²", "B) a + b = c", "C) a² - b² = c²", "D) a² + b² = 2c"],
                "correct_answer": "A",
                "explanation": "In any right-angled triangle, the square of the hypotenuse (c) is equal to the sum of squares of the other two sides (a² + b²)."
            },
            {
                "id": 2,
                "question": "Which side of a right triangle is the longest?",
                "options": ["A) Adjacent", "B) Opposite", "C) Hypotenuse", "D) Base"],
                "correct_answer": "C",
                "explanation": "The hypotenuse is the side opposite to the 90-degree right angle and is always the longest side."
            },
            {
                "id": 3,
                "question": "If the two shorter sides of a right triangle are 3 and 4, what is the length of the hypotenuse?",
                "options": ["A) 7", "B) 5", "C) 6", "D) 25"],
                "correct_answer": "B",
                "explanation": "3² + 4² = 9 + 16 = 25. The square root of 25 is 5."
            }
        ]

    return [
        {
            "id": 1,
            "question": f"What is the core significance of {topic_or_passage[:30]}?",
            "options": [
                f"A) It provides essential foundational principles",
                f"B) It has no practical application",
                f"C) It is only used in fictional contexts",
                f"D) It was deprecated in ancient times"
            ],
            "correct_answer": "A",
            "explanation": f"Understanding {topic_or_passage[:30]} is fundamental to mastering the broader subject area."
        },
        {
            "id": 2,
            "question": f"How is knowledge of {topic_or_passage[:30]} typically applied?",
            "options": [
                "A) Randomly without methodology",
                "B) Through systematic study and practice",
                "C) Exclusively by computer algorithms",
                "D) Only during theoretical exams"
            ],
            "correct_answer": "B",
            "explanation": "Effective application requires disciplined study and hands-on practice."
        },
        {
            "id": 3,
            "question": "Which learning technique best reinforces this topic?",
            "options": [
                "A) Passive memorization",
                "B) Active problem solving and conceptual review",
                "C) Skipping foundational chapters",
                "D) Ignoring real-world examples"
            ],
            "correct_answer": "B",
            "explanation": "Active recall and practical problem-solving lead to long-term concept retention."
        }
    ]
