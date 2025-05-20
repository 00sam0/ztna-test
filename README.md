# ZTNA FastAPI App

This is a simple Zero Trust Network Access (ZTNA)-style API microservice using FastAPI, JWT, and role-based access control.

## 🔐 Features
- User registration via secure API
- JWT login
- Role-based access control (`admin`, `user`, `editor`)
- PostgreSQL-ready
- Dockerized for deployment

## 🚀 Deploy on Render

1. [Create a PostgreSQL DB on Render](https://render.com/docs/databases)
2. Fork this repo or upload it to GitHub
3. Click "New Web Service" on Render
4. Connect your GitHub repo
5. Choose `Docker` environment
6. Set the following environment variables:
   - `DATABASE_URL`
   - `SECRET_KEY`

Done! Render will build and host your API.

## 🧪 Local Dev

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📦 API Endpoints

- `POST /register`: Register a new user
- `POST /login`: Get JWT token
- `GET /`: Basic test route
