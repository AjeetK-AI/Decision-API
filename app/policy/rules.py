#Let make Rules that define refunds,return, cancellation,warranty etc.
from pydantic import BaseModel, Field
from typing import Any, List, Optional  #Any variable can contain almost any Python type string,integer etc.
                                        

class PolicyCondition(BaseModel):
    #rule_id: str
    field:str
    operator:str
    value: Any 
    #action: str

class PolicyRule(BaseModel):
     rule_id:str
     action: str

     conditions: List[PolicyCondition] = Field(default_factory=list)

     decision:str
     action: str 

     priority: int = 0

    #min_amount: float | None = None
    #max_amount: float | None = None

    #decision: str
    #reason: str

    conditions: list[str] = Field(default_factory=list)

    priority: int = 0

"""
POLICY_RULES = [

    PolicyRule(
        rule_id="refund_001",
        action="refund",
        max_amount=9999.99,
        decision="APPROVE",
        reason="Refunds below ₹10,000 may be approved automatically when evidence is present and no fraud or exception exists.",
        priority=0
    ),

    PolicyRule(
        rule_id="refund_002",
        action="refund",
        min_amount=10000,
        max_amount=50000,
        decision="MANAGER_APPROVAL",
        reason="Refunds from ₹10,000 through ₹50,000 require manager approval.",
        priority=0
    ),

    PolicyRule(
        rule_id="refund_003",
        action="refund",
        min_amount=50000.01,
        decision="FINANCE_APPROVAL",
        reason="Refunds above ₹50,000 require Finance approval.",
        priority=0
    ),

    PolicyRule(
        rule_id="refund_004",
        action="refund",
        max_amount=9999.99,
        decision="MANAGER_APPROVAL",
        reason="Requests submitted after 30 days require manager review.",
        conditions=["days_since_purchase > 30"],
        priority=50
    ),

    PolicyRule(
        rule_id="fraud_001",
        action="refund",
        decision="FRAUD_REVIEW",
        reason="Fraud indicators require Fraud or Risk team review.",
        conditions=["fraud_indicator == true"],
        priority=100
    )
]
"""