#Let make Rules that define refunds,return, cancellation,warranty etc.
from pydantic import BaseModel, Field
from typing import Any  #Any variable can contain almost any Python type string,integer etc.
                                        

class PolicyCondition(BaseModel):
    field:str
    operator:str
    value: Any 
    

class PolicyRule(BaseModel):
     rule_id:str
     action: str
     conditions: list[PolicyCondition] = Field(default_factory=list)
     decision:str
     action: str 
     reason: str
     priority: int = 0