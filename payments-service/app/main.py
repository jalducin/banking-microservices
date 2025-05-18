from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(title="Payments Service", version="1.0")

# Modelos de petición
class BillPayment(BaseModel):
    account_id: str = Field(..., example="ACC-1001")
    biller: str = Field(..., example="Electric Company")
    amount: float = Field(..., gt=0)

class Transfer(BaseModel):
    from_account: str
    to_account: str
    amount: float

# Simulación en memoria
db_accounts = {"ACC-1001": 1000.0}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/payments/bill")
async def pay_bill(payment: BillPayment):
    if payment.account_id not in db_accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    if db_accounts[payment.account_id] < payment.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    db_accounts[payment.account_id] -= payment.amount
    return {"status": "paid", "remaining_balance": db_accounts[payment.account_id]}

@app.post("/payments/transfer")
async def transfer_funds(txn: Transfer):
    if txn.from_account not in db_accounts or txn.to_account not in db_accounts:
        raise HTTPException(status_code=404, detail="One or both accounts not found")
    if db_accounts[txn.from_account] < txn.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    db_accounts[txn.from_account] -= txn.amount
    db_accounts[txn.to_account] += txn.amount
    return {"status": "transferred", "from_balance": db_accounts[txn.from_account], "to_balance": db_accounts[txn.to_account]}