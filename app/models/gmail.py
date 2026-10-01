#Create Gmail Request Model 

from pydantic import BaseModel


class EmailRequest(BaseModel):
    subject: str
    body: str
    amount: float | None = None
    days_since_purchase: int | None = None
    evidence_present: bool = True
    fraud_indicator: bool = False


class DecisionResponse(BaseModel):
    intent: str
    risk: str
    decision: str
    request_approval: bool
