import json 

from app.policy.rules import PolicyRule 

def extract_policy_rules(text : str)->list[PolicyRule]:

   """
Convert policy text into structured PolicyRule objects.

This function is intentionally not tied to refund, return,
fraud, or any other specific business policy.
"""

    # Temporary placeholder.
    #
    # The next step will connect an LLM here to convert
    # arbitrary policy text into structured JSON.
    #
    # For now, we return no rules rather than hardcoding
    # business rules.

   return []








