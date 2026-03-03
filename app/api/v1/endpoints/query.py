from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter()

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, example='How many male patients')

class QueryResponse(BaseModel):
    question: str
    answer: str

@router.post("/", response_model=QueryResponse)
def run_check(payload: QueryRequest):
    try:
        llm_answer = f"Question: {payload.question}"

        return QueryResponse(
            question=payload.question,
            answer=llm_answer
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
