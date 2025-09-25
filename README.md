# Wholesalers.AI (Mono Repo)
Frontend: Next.js (Vercel) • Backend: FastAPI (Fly.io)

## Deploy (quick)
Frontend → Vercel (project root = `frontend`)
Backend  → Fly.io (cd `backend` → `fly launch` → `fly deploy`)

## Local
### Backend
cd backend
python -m venv .venv && . .venv/Scripts/activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

### Frontend
cd frontend
pnpm i
pnpm dev

Open:
- Backend docs: http://127.0.0.1:8000/docs
- Frontend:     http://localhost:3000
