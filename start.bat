@echo off
title StudyFinder India Server
echo ===============================================================
echo     STUDYFINDER INDIA - The Ultimate Education Platform
echo     Tagline: "Find. Compare. Rank. Choose. Succeed."
echo ===============================================================
echo.
echo Starting StudyFinder India web application on http://localhost:8000 ...
echo Press Ctrl+C in this terminal window to stop the server anytime.
echo.
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
pause
