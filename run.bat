@echo off
title EduGenie AI Server
echo =========================================================
echo   EduGenie: Google Gemini Powered Learning Assistant
echo   Naan Mudhalvan / IBM SkillsBuild Project
echo   Developed by Priya Dharshini and Team
echo =========================================================
echo.
echo Checking & installing dependencies...
pip install -r requirements.txt
echo.
echo Starting EduGenie Server on http://127.0.0.1:8000 ...
echo Press Ctrl+C to stop the server.
echo.
uvicorn main:app --reload --host 127.0.0.1 --port 8000
pause
