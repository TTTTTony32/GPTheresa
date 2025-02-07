@echo off
python -m venv venv
venv\Scripts\activate.bat
uvicorn MiddleAPI:app --host 0.0.0.0 --port 8000