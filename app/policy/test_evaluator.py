from app.policy.store import active_policy_rules
from app.policy.evaluator import find_matching_rules


def test_scenario(name, facts):

    matches = find_matching_rules(
        active_policy_rules,
        "return",
        facts
    )

    print(f"\n{name}")
    print("-" * 40)

    if not matches:
        print("No matching rules")
        return

    for rule in matches:
        print(
            rule.rule_id,
            "|",
            rule.decision,
            "|",
            rule.reason
        )


# Scenario 1: Return within 7 days
test_scenario(
    "Scenario 1 - 5 days",
    {
        "days_since_purchase": 5,
        "fraud_indicator": False
    }
)


# Scenario 2: Return after 7 days
test_scenario(
    "Scenario 2 - 10 days",
    {
        "days_since_purchase": 10,
        "fraud_indicator": False
    }
)


# Scenario 3: Fraud
test_scenario(
    "Scenario 3 - Fraud",
    {
        "days_since_purchase": 5,
        "fraud_indicator": True
    }
)