from pydantic import BaseModel
from typing import Optional, List, Dict

class MessageRequest(BaseModel):
    prompt: str
    industry: Optional[str] = None
    target_audience: Optional[str] = None
    tone: Optional[str] = None

class MessageResponse(BaseModel):
    message: str

class MultipleMessagesRequest(BaseModel):
    prompt: str
    count: int = 3
    industry: Optional[str] = None
    target_audience: Optional[str] = None
    tone: Optional[str] = None

class MultipleMessagesResponse(BaseModel):
    messages: List[str]

class MessageAnalysisRequest(BaseModel):
    message: str

class MessageAnalysisResponse(BaseModel):
    message: str
    analysis: str

class ServiceStatusResponse(BaseModel):
    is_initialized: bool
    api_available: bool