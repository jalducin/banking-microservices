from fastapi import FastAPI
from pydantic import BaseModel, Field
import random

app = FastAPI(title="Risk Service", version="1.0")

class RiskRequest(BaseModel):
    customer_id: str = Field(..., example="CUST-0001")

class RiskResponse(BaseModel):
    score: int
    risk_level: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/score/{customer_id}", response_model=RiskResponse)
async def get_score(customer_id: str):
    # Simulación de cálculo de score
    score = random.randint(300, 850)
    level = ("low" if score >= 700 else "medium" if score >= 500 else "high")
    return RiskResponse(score=score, risk_level=level)