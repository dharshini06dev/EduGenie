import os
from gemini_helper import generate_text_with_rotation

def get_learning_recommendations(topic: str, language: str = "English") -> str:
    """
    Generates a personalized, step-by-step learning roadmap from beginner to advanced levels
    with timelines and curated resources.
    """
    sys_prompt = f"""
    You are EduGenie's Curriculum & Career Learning Path Advisor.
    Create a structured, step-by-step learning roadmap for the requested topic: '{topic}'.
    
    Target Language: {language} (Options: English, Thanglish, or Tamil).
    
    Structure the roadmap clearly:
    1. 🎯 Level 1: Beginner / Fundamentals (Weeks 1-2) - Core basics & simple exercises
    2. 🚀 Level 2: Intermediate Concepts (Weeks 3-5) - Practical tools & hands-on mini-projects
    3. 🏆 Level 3: Advanced Mastery (Weeks 6-8) - Architecture, optimization, and capstone project
    4. 📚 Recommended Free Resources (Official docs, YouTube channels, practice sites)
    """
    
    response = generate_text_with_rotation(topic, sys_prompt)
    if response:
        return response

    # Smart Fallback Roadmap
    return f"""### 🗺️ Structured Learning Path: {topic}

#### 🎯 Level 1: Beginner Fundamentals (Weeks 1–2)
- **Topics Covered:** Introduction to {topic}, foundational syntax, core terminology, and development environment setup.
- **Milestone Project:** Build a basic hello-world or simple CLI program using {topic} concepts.
- **Estimated Time:** 10 hours/week.

#### 🚀 Level 2: Intermediate Practical Mastery (Weeks 3–5)
- **Topics Covered:** Data structures, design patterns, modular architecture, and API integrations.
- **Milestone Project:** Create a functional end-to-end mini-application.
- **Estimated Time:** 12 hours/week.

#### 🏆 Level 3: Advanced & Industry Readiness (Weeks 6–8)
- **Topics Covered:** Performance tuning, security best practices, CI/CD, and real-world deployment.
- **Capstone Project:** Full-stack production-ready portfolio project with documentation.
- **Estimated Time:** 15 hours/week.

#### 📚 Curated Learning Resources:
- 📖 **Official Documentation:** Developer guides & tutorials
- 🎥 **Video Courses:** FreeCodeCamp & Coursera playlists
- 💻 **Hands-on Labs:** LeetCode, GitHub open-source repositories & documentation
"""
