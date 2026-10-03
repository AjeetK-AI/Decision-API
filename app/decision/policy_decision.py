from app.policy.store import active_policy_rules 
from app.policy.evaluator import find_matching_rules


def make_policy_decision(action: str,facts: dict):
    matches = find_matching_rules(
            active_policy_rules,
            action,
            facts 
    )

    if not matches:
        return{
        "decision": "NEED_APPROVAL",
         "request_approval": True,
         "reason": "No matching policy rule was found.",
        "rules_used": []
        }
    # Highest-priority rule wins
    rule = matches[0]

    return {
        "decision": rule.decision,
        "request_approval": rule.decision != "APPROVE",
        "reason": rule.reason,
        "rules_used": [rule.rule_id]
    }