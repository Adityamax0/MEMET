# 💜 Memet — Feel Heard. Always.

> An emotionally intelligent AI companion that listens, validates, and responds with genuine warmth.

![Live](https://img.shields.io/badge/Live-memet--lake.vercel.app-blueviolet?style=for-the-badge)
![Backend](https://img.shields.io/badge/Backend-Render-46E3B7?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-Groq%20LLaMA%203.3%2070B-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live%20%26%20Running-success?style=for-the-badge)

---

## 🌐 Live Demo

**Frontend:** [memet-lake.vercel.app](https://memet-lake.vercel.app)  
**Backend API:** [memet-2nmm.onrender.com](https://memet-2nmm.onrender.com)  
**API Docs:** [memet-2nmm.onrender.com/docs](https://memet-2nmm.onrender.com/docs)

---

## ✨ What is Memet?

Memet is a full-stack emotionally intelligent AI companion built for people who need a safe, non-judgmental space to process complex emotions. Unlike standard chatbots that offer generic comfort, Memet uses **Reflective Inquiry** and **Psychological Reframing** to genuinely understand what you're feeling.

Certified **98% EQ Score** — tested against 5 real-world emotional stress tests including success-grief, impulse control, existential longing, vulnerability, and friendship envy.

> *"It's like having an external prefrontal cortex."* — The Gemini Protocol Evaluation

---

## 🏗️ Architecture

```
┌─────────────────────┐        ┌──────────────────────┐        ┌─────────────────┐
│   Frontend          │  HTTP  │   Backend            │  API   │   Groq Cloud    │
│   Vercel            │ ──────▶│   Render (FastAPI)   │ ──────▶│   LLaMA 3.3 70B │
│   index.html        │        │   main.py            │        │                 │
└─────────────────────┘        └──────────────────────┘        └─────────────────┘
```

| Layer | Tech | Host |
|-------|------|------|
| Frontend | HTML / CSS / JavaScript (single file) | Vercel |
| Backend | Python + FastAPI + Uvicorn | Render |
| AI Model | Groq LLaMA 3.3 70B (fast inference) | Groq Cloud |
| Styling | Pure CSS — glassmorphism + dreamy purple | — |

---

## 💻 Frontend Features

- 🎨 **3 pages** — Home, Chat, About
- ✨ **120 floating particles** on canvas background
- 🖱️ **Custom purple cursor** with trail effect
- 🌈 **Animated gradient** background with 3 glowing orbs
- 💬 **Floating chat preview** card on hero section
- 🔮 **Glassmorphism navbar** (pill style)
- 💜 **Mood selector chips** — Sad / Anxious / Frustrated / Numb / Okay / Good
- 🚨 **Crisis detection** with Indian mental health helplines
- ⏳ **Typing indicator** animation
- 🌙 **Dreamy soft purple/lavender** theme throughout

---

## 🔧 Backend API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Server info |
| `GET` | `/health` | Health check |
| `POST` | `/chat` | Send message → get AI reply |

### `/chat` Request Body
```json
{
  "message": "I feel like no one understands me",
  "history": [...last 12 messages],
  "mood": "Sad"
}
```

### `/chat` Response
```json
{
  "reply": "That sounds really isolating..."
}
```

---

## 🚀 Run Locally

### Prerequisites
- Python 3.10+
- Groq API key from [console.groq.com](https://console.groq.com) (free)

### Backend Setup
```bash
git clone https://github.com/Adityamax0/MEMET.git
cd MEMET

# Create .env file
echo GROQ_API_KEY=your_gsk_key_here > .env

# Install dependencies
pip install -r requirements.txt

# Start server
python -m uvicorn main:app --reload
```

Backend runs at `http://localhost:8000`

### Frontend
Just open `index.html` in your browser — or deploy to Vercel.

---

## 📁 Repository Structure

```
MEMET/
├── index.html          # Full frontend — single file app
├── main.py             # FastAPI backend
├── requirements.txt    # Python dependencies
└── .env                # (local only, never commit) — GROQ_API_KEY
```

---

## 🧠 AI Configuration

- **Model:** `llama-3.3-70b-versatile`
- **Temperature:** `0.85` (warm, expressive)
- **Max tokens:** `320` per reply
- **Context window:** Last 12 messages sent with each request
- **System prompt:** Validates feelings first, uses reflective inquiry, avoids toxic positivity

---

## 📊 EQ Evaluation Results

| Criteria | Rating | Notes |
|----------|--------|-------|
| Empathy Accuracy | 10/10 | Identified "The Arrival Fallacy" correctly |
| Conflict Resolution | 9.5/10 | Balanced validation with Tough Love |
| Philosophical Depth | 10/10 | Used poetic metaphors naturally |
| Identity Stability | 10/10 | Secure about its non-human nature |

**Overall: 98% — Certified High-EQ Assistant** ✅  
*Signed: The Gemini Protocol, March 4, 2026*

---

## 🗺️ Roadmap

- [x] Frontend live on Vercel
- [x] Backend deployed on Render
- [x] Frontend connected to backend
- [x] Crisis detection with helplines
- [ ] User login + signup (Supabase)
- [ ] Chat memory across sessions
- [ ] Mood history timeline
- [ ] Mobile app (PWA)

---

## 👨‍💻 Built By

**Aditya Pandey** — 2nd Year Engineering Student  
GitHub: [@Adityamax0](https://github.com/Adityamax0)

> Built this entire full-stack app — frontend, backend, deployment — in a single day. 💜

---

## 📄 License

MIT License — free to use, modify, and share.
