@echo off
title SnapClass AI Attendance App
echo ========================================================
echo   Starting SnapClass AI Attendance App (Streamlit)
echo ========================================================
cd /d "%~dp0"

if exist "..\.venv\Scripts\python.exe" (
    "..\.venv\Scripts\python.exe" app.py
) else (
    python app.py
)
pause
