from app.policy.rules import PolicyRule, PolicyCondition


# Active policy rules
active_policy_rules = [

    PolicyRule(
        rule_id="return_001",
        action="return",
        conditions=[
            PolicyCondition(
                field="days_since_purchase",
                operator="<=",
                value=7
            )
        ],
        decision="APPROVE",
        reason="Products can be returned within 7 days",
        priority=10
    ),

    PolicyRule(
        rule_id="return_002",
        action="return",
        conditions=[
            PolicyCondition(
                field="days_since_purchase",
                operator=">",
                value=7
            )
        ],
        decision="MANAGER_APPROVAL",
        reason="Return after 7 days requires Manager Approval",
        priority=50
    ),

    PolicyRule(
        rule_id="fraud_001",
        action="return",
        conditions=[
            PolicyCondition(
                field="fraud_indicator",
                operator="==",
                value=True
            )
        ],
        decision="FRAUD_REVIEW",
        reason="FRAUD INDICATOR",
        priority=100
    ),

]