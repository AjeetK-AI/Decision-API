import re


def extract_policy_rules(
    policy_text: str,
) -> list[dict[str, str]]:
    """
    Split policy text into individual policy rules.

    This parser does not interpret the meaning of a rule.
    It only identifies the rule ID and rule text.

    The extracted rule blocks are passed to the LLM parser.
    """

    rule_blocks: list[dict[str, str]] = []

    pattern = re.compile(
        r"Rule\s+([0-9]+(?:\.[0-9]+)*)\s*:\s*"
        r"(.*?)(?=\s*Rule\s+[0-9]+(?:\.[0-9]+)*\s*:|\Z)",
        re.IGNORECASE | re.DOTALL,
    )

    matches = pattern.findall(policy_text)

    for rule_id, rule_text in matches:

        cleaned_text = " ".join(
            rule_text.split()
        )

        rule_blocks.append(
            {
                "rule_id": rule_id,
                "text": cleaned_text,
            }
        )

    return rule_blocks