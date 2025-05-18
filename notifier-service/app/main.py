
from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel, EmailStr, Field
from .utils import send_email

app = FastAPI(title="Notifier Service", version="1.0")

class Notification(BaseModel):
    to_email: EmailStr
    subject: str
    message: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/notify/email")
async def notify_email(notification: Notification, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, notification.to_email, notification.subject, notification.message)
    return {"status": "queued"}