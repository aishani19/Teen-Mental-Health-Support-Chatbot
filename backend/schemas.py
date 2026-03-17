from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class Message(BaseModel):
    text: str
    user_id: int


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=2000)
    history: Optional[List[str]] = []
    user_id: Optional[int] = None


class ChatResponse(BaseModel):
    reply: str
    user_id: Optional[int]
    risk_level: int
    topics: List[str]
    created_at: datetime