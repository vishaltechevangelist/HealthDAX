from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime

@router.get("/", response_model=HealthResponse)
def health_check():
    return HealthResponse(status='ok', timestamp=datetime.utcnow())