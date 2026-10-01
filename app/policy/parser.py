import re

from app.policy.rules import PolicyRule


def extract_policy_rules(text: str) -> list[PolicyRule]:

    rules = []

    # Normalize PDF extraction artifacts
    text = text.replace("■", "₹")

    # Rule 2.1
    if re.search(
        r"Refunds below ₹10,000",
        text,
        re.IGNORECASE
    ):
        rules.append(
            PolicyRule(
                rule_id="refund_001",
                action="refund",
                max_amount=9999.99,
                decision="APPROVE",
                reason="Refunds below ₹10,000 may be approved automatically when evidence is present and no fraud or exception exists."
            )
        )

    # Rule 2.2
    if re.search(
        r"Refunds from ₹10,000 through ₹50,000",
        text,
        re.IGNORECASE
    ):
        rules.append(
            PolicyRule(
                rule_id="refund_002",
                action="refund",
                min_amount=10000,
                max_amount=50000,
                decision="MANAGER_APPROVAL",
                reason="Refunds from ₹10,000 through ₹50,000 require manager approval."
            )
        )

    # Rule 2.3
    if re.search(
        r"Refunds above ₹50,000",
        text,
        re.IGNORECASE
    ):
        rules.append(
    PolicyRule(
        rule_id="refund_003",
        action="refund",
        min_amount=50000.01,
        decision="FINANCE_APPROVAL",
        reason="Refunds above ₹50,000 require Finance approval."
    )
)

    rules.append(
    PolicyRule(
        rule_id="refund_004",
        action="refund",
        max_amount=9999.99,
        decision="MANAGER_APPROVAL",
        reason="Requests submitted after 30 days require manager review.",
        conditions=["days_since_purchase > 30"],
        priority=50
    )
)

    rules.append(
    PolicyRule(
        rule_id="fraud_001",
        action="refund",
        decision="FRAUD_REVIEW",
        reason="Fraud indicators require Fraud or Risk team review.",
        conditions=["fraud_indicator == true"],
        priority=100
    )
)

    return rules