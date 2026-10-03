from app.services.llm_policy_parser import (
    extract_policy_rules_with_llm,
)


policy_text = """
Company Product Return and Refund Policy

Customers may return products within 7 days of purchase.

Returns submitted after 7 days require manager approval.

Refunds below ₹10,000 may be approved automatically when
required evidence is present and no fraud indicator exists.

Refunds from ₹10,000 through ₹50,000 require manager approval.

Refunds above ₹50,000 require Finance approval.

Fraud indicators require review by the Fraud or Risk team.
"""


rules = extract_policy_rules_with_llm(policy_text)


print("\nRules extracted by LLM:")
print("=" * 60)


for rule in rules:

    print("\nRule ID:", rule.rule_id)
    print("Action:", rule.action)
    print("Conditions:", rule.conditions)
    print("Decision:", rule.decision)
    print("Reason:", rule.reason)
    print("Priority:", rule.priority)