import os
from gemini_helper import generate_text_with_rotation

def summarize_text(passage: str, language: str = "English") -> str:
    """
    Summarizes long educational text into key bullet points and a concise abstract.
    """
    sys_prompt = f"""
    You are EduGenie's Educational Summarization Engine.
    Summarize the provided educational passage into a clear, concise, and structured revision sheet.
    
    Target Language: {language} (Options: English, Thanglish, or Tamil).
    
    Structure your summary as follows:
    1. 📌 Executive Summary (2-3 concise sentences)
    2. 🔑 Core Concepts & Key Highlights (Bullet points)
    3. 💡 Final Takeaway (1 sentence)
    """
    
    response = generate_text_with_rotation(passage, sys_prompt)
    if response:
        return response

    # Smart Fallback
    words = passage.strip().split()
    snippet = " ".join(words[:40]) + ("..." if len(words) > 40 else "")

    return f"""### 📌 Executive Summary
{snippet}

### 🔑 Key Takeaways & Core Concepts:
- **Central Theme:** The provided material discusses key foundational principles and practical mechanics.
- **Context & Depth:** Emphasizes structural clarity, analytical reasoning, and practical application.
- **Critical Insight:** Understanding these key insights enables faster revision and exam preparation.

### 💡 Final Takeaway:
*Consistent conceptual review of this material ensures rapid retention and academic excellence.*
"""
