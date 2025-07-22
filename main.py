from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from database import logs, save_log

app = FastAPI()

class Log(BaseModel):
    timestamp: str
    type: str
    message: str

@app.post("/log")
def receive_log(log: Log):
    save_log(log)
    return {"status": "Log received"}

@app.get("/logs", response_model=List[Log])
def get_logs():
    return logs
