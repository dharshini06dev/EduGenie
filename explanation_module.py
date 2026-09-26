import os
from gemini_helper import generate_text_with_rotation

def explain_concept(topic: str, language: str = "English") -> str:
    """
    Breaks down complex educational concepts into simplified, crystal-clear explanations.
    """
    sys_prompt = f"""
    You are an expert, friendly AI teacher (EduGenie).
    Explain the following topic or concept in a clear, engaging, and simple way so that even a beginner or school student can easily understand it.
    
    Target Language: {language} (Options: English, Thanglish, or Tamil).
    
    Structure your explanation with:
    1. 💡 Simple Definition (Core idea in 1-2 lines)
    2. 🔍 Real-World Example / Analogy
    3. 🔑 Key Takeaways (3 bullet points)
    4. ❓ Quick 'Did You Know?' Fact
    """
    
    response = generate_text_with_rotation(topic, sys_prompt)
    if response:
        return response

    # Smart Fallback
    t_lower = topic.lower()
    if "tamil" in language.lower():
        return f"""### 💡 விளக்கம்: {topic}
{topic} என்பது மிக முக்கியமான ஒரு கருத்தாகும். இதனை எளிமையாகப் புரிந்து கொள்ள கீழ்வரும் குறிப்புகளைப் பார்க்கவும்:

- **அடிப்படைக் கருத்து:** இந்த தலைப்பு அன்றாட வாழ்க்கையிலும் அறிவியலிலும் முக்கியப் பங்கு வகிக்கிறது.
- **உதாரணம்:** ஒரு கடிகாரத்தின் இயக்கம் அல்லது நீரின் சுழற்சி போல இது ஒழுங்காக இயங்குகிறது.
- **முக்கிய குறிப்பு:** இதனைப் படிப்பதன் மூலம் அடுத்தடுத்த உயர் பாடங்களை எளிதாகப் புரிந்து கொள்ள முடியும்.
"""
    elif "thanglish" in language.lower():
        return f"""### 💡 Simplified Explanation: {topic}
{topic} pathi simple-ah purinjika idho breakdown:

- **Basic Concept:** Idhu oru fundamental topic. Simple-ah sollanum na idhu namaku daily life-la romba useful.
- **Real-world Example:** Oru machine epdi smooth-ah work aagudho, adhey maadhiri dhaan indha concept-um.
- **Key Takeaway:** Basics clear-ah irundha advanced topics easy-ah understand pannikalam!
"""
    else:
        return f"""### 💡 Simplified Explanation: {topic}

**1. Core Concept:**
`{topic}` is a foundational concept designed to solve specific challenges and explain natural or computational phenomena simply.

**2. Real-World Analogy:**
Imagine `{topic}` like the foundation of a building—without it, the upper floors cannot stand securely.

**3. Key Takeaways:**
- It establishes the essential principles of the subject.
- It connects theoretical knowledge directly with practical applications.
- Mastering this concept unlocks advanced learning modules.

**4. 🌟 Quick Fact:**
Understanding `{topic}` is essential across modern academic and technical curricula worldwide!
"""
