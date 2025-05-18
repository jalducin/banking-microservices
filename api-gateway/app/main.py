from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field
import httpx

app = FastAPI(title="API Gateway", version="1.0")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

class LoanRequest(BaseModel):
    customer_id: str = Field(..., example="CUST-0001")
    amount: float = Field(...)
    term_months: int = Field(...)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/loans/validate")
async def validate_loan(request: LoanRequest, token: str = Depends(oauth2_scheme)):
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "http://loans-service:8000/loans/validate", 
            json=request.dict(), 
            headers={"Authorization": f"Bearer {token}"}
        )
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()