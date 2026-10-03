import json

from app.llm.client import client
from app.llm.prompts import POLICY_EXTRACTION_PROMPT
from app.policy.rules import PolicyRule


def extract_policy_rules_with_llm(
    policy_text: str,
) -> list[PolicyRule]:

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        response_format={
            "type": "json_object"
        },
        messages=[
            {
                "role": "system",
                "content": str(POLICY_EXTRACTION_PROMPT),
            },
            {
                "role": "user",
                "content": str(policy_text),
            },
        ],
    )

    content = response.choices[0].message.content

    if not content:
        raise ValueError(
            "LLM returned an empty response"
        )

    data = json.loads(content)

    rules_data = data.get("rules", [])

    return [
        PolicyRule(**rule)
        for rule in rules_data
    ]