from fastapi import FastAPI
from app.routes import register, login
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(register.router)
app.include_router(login.router)

@app.get("/")
def root():
    return {"message": "ZTNA FastAPI up and running"}
