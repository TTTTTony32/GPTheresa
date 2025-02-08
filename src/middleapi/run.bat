@echo off
python -m venv venv
"venv\Scripts\pip.exe" install -r requirements.txt
"venv\Scripts\python.exe" -m uvicorn MiddleAPI:app --host 0.0.0.0 --port 8000