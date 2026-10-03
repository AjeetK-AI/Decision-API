from app.models.gmail import EmailRequest, DecisionResponse
from app.decision.policy_decision import make_policy_decision


def decide(email: EmailRequest) -> DecisionResponse:

    text = (
        email.subject + " " + email.body
    ).lower()

    # 1. Detect intent

    if "refund" in text:
        intent = "refund"

    elif "meeting" in text:
        return DecisionResponse(
            intent="meeting",
            risk="low",
            decision="reply",
            request_approval=False
        )

    elif "unsubscribe" in text:
        return DecisionResponse(
            intent="unsubscribe",
            risk="low",
            decision="archive",
            request_approval=False
        )

    else:
        return DecisionResponse(
            intent="unknown",
            risk="medium",
            decision="review",
            request_approval=True
        )

    # 2. If refund, check company policy

    if intent == "refund":

    # 2. If refund, check company policy

     if intent == "refund":

      facts = {
        "amount": email.amount,
        "days_since_purchase": email.days_since_purchase,
        "evidence_present": email.evidence_present,
        "fraud_indicator": email.fraud_indicator
    }

      policy_result = make_policy_decision(
        action="refund",
        facts=facts
    )

    return DecisionResponse(
        intent="refund",
        risk="normal",
        decision=policy_result["decision"],
        request_approval=policy_result["request_approval"]
    )

    
        # 3. No matching policy

    if rule is None:
            return DecisionResponse(
                intent="refund",
                risk="unknown",
                decision="NEED_APPROVAL",
                request_approval=True
            )

        # 4. Policy matched

    return DecisionResponse(
            intent="refund",
            risk="normal",
            decision=rule.decision,
            request_approval=rule.decision != "APPROVE"
        )