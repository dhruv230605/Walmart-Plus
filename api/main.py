# api/main.py
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"} 