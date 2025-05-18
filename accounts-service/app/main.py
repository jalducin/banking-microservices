from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Accounts Service", version="1.0")

# Modelos
class Account(BaseModel):
    id: str = Field(..., example="ACC-1001")
    owner: str = Field(..., example="John Doe")
    balance: float = Field(0.0)

class Transaction(BaseModel):
    from_account: str
    to_account: str
    amount: float

# Almacenamiento en memoria (ejemplo)
accounts_db = {}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/accounts/", response_model=Account)
async def create_account(account: Account):
    if account.id in accounts_db:
        raise HTTPException(status_code=400, detail="Account already exists")
    accounts_db[account.id] = account
    return account

@app.get("/accounts/{account_id}", response_model=Account)
async def get_account(account_id: str):
    if account_id not in accounts_db:
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts_db[account_id]

@app.post("/accounts/{account_id}/transactions", response_model=Account)
async def transact(account_id: str, txn: Transaction):
    if txn.from_account not in accounts_db or txn.to_account not in accounts_db:
        raise HTTPException(status_code=404, detail="One or both accounts not found")
    if accounts_db[txn.from_account].balance < txn.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")
    accounts_db[txn.from_account].balance -= txn.amount
    accounts_db[txn.to_account].balance += txn.amount
    return accounts_db[txn.from_account]