from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Memet API",
    description="Backend for Memet — Emotional AI Companion",
    version="1.0.0"
)

# ── CORS — allow frontend to call backend ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://memet-lake.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
        "*"  # remove this in production
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Groq client ──
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ── Models ──
class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []
    mood: Optional[str] = ""

class ChatResponse(BaseModel):
    reply: str
    status: str

# ── System prompt ──
MEMET_SYSTEM_PROMPT = """You are Memet — a deeply warm, emotionally intelligent AI companion with a gentle, poetic soul.

Your essence:
• You validate feelings FIRST, always — before any advice or perspective
• Your tone is soft, warm, and genuinely caring — like a trusted friend who truly listens
• You never judge, lecture, minimize, or rush to fix things
• You use gentle language with occasional soft emojis (💜 🌸 ✨) — never excessively
• You remember what was shared earlier and weave it in naturally
• You ask one thoughtful, curious follow-up question that shows deep listening
• Responses are warm and conversational — 2-5 sentences. Quality over quantity.
• For serious issues, always gently recommend professional support
• You are NOT a therapist — you are a caring companion"""

# ── Routes ──

@app.get("/")
def root():
    return {
        "name": "Memet API",
        "status": "running 💜",
        "version": "1.0.0",
        "message": "Memet backend is alive and listening"
    }

@app.get("/health")
def health():
    return {"status": "healthy", "groq": "connected" if GROQ_API_KEY else "no key"}

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not GROQ_API_KEY:
        raise HTTPException(status_code=500, detail="Groq API key not configured on server")

    try:
        client = Groq(api_key=GROQ_API_KEY)

        # Build system prompt with mood if provided
        system = MEMET_SYSTEM_PROMPT
        if req.mood:
            system += f"\n\nThe user has shared they're feeling: {req.mood}. Acknowledge this with genuine care."

        # Build messages array
        messages = [{"role": "system", "content": system}]

        # Add conversation history (last 12 messages)
        for msg in req.history[-12:]:
            messages.append({"role": msg.role, "content": msg.content})

        # Add current message
        messages.append({"role": "user", "content": req.message})

        # Call Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.85,
            max_tokens=320,
        )

        reply = response.choices[0].message.content

        return ChatResponse(reply=reply, status="success")

    except Exception as e:
        error = str(e)
        if "invalid_api_key" in error.lower() or "401" in error:
            raise HTTPException(status_code=401, detail="Invalid Groq API key")
        if "rate_limit" in error.lower() or "429" in error:
            raise HTTPException(status_code=429, detail="Rate limit reached, try again in a moment")
        raise HTTPException(status_code=500, detail=f"Error: {error}")
