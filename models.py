from pydantic import BaseModel

class Log(BaseModel):
    timestamp: str
    type: str
    message: str
