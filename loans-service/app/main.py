from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import httpx

app = FastAPI(title="Loans Service", version="1.0")

# Modelos
class CreditRequest(BaseModel):
    customer_id: str = Field(..., example="CUST-0001")
    amount: float = Field(..., gt=0)
    term_months: int = Field(..., gt=0)

class CreditResponse(BaseModel):
    approved: bool
    score: float
    reason: str = None

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/loans/validate", response_model=CreditResponse)
async def validate_credit(request: CreditRequest):
    # Placeholder: Simula llamada a Risk Service
    score = 750  # ej. respuesta mock
    approved = score >= 700 and request.amount <= 50000
    reason = None if approved else "Rechazado por score o monto"
    return CreditResponse(approved=approved, score=score, reason=reason)

@app.post("/loans/calculate-interest")
async def calculate_interest(request: CreditRequest):
    # Cálculo simple de interés
    tasa_anual = 0.05
    monto_total = request.amount * (1 + tasa_anual * (request.term_months / 12))
    return {"total": monto_total}