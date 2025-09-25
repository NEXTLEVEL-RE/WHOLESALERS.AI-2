import os, time
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from .security.auth import issue_token, verify_token

load_dotenv()

app = FastAPI(title="Wholesalers.AI GPT-Core", version="0.1.0")
START = time.time()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@app.get("/healthz")
def healthz():
    return {"ok": True, "uptime_s": round(time.time() - START, 1)}

@app.get("/readyz")
def readyz():
    # add DB checks later; returns 200 now
    return {"ready": True}

@app.post("/auth/issue")
def auth_issue(sub: str, role: str = "owner", ttl: int = 604800):
    token = issue_token(sub=sub, role=role, ttl=ttl)
    return {"token": token}

@app.post("/chat")
def chat(req: ChatRequest, user=Depends(verify_token)):
    # Minimal echo; replace with orchestrator later
    reply = f"Hello {user['sub']}! You said: {req.message}"
    return {"reply": reply}
