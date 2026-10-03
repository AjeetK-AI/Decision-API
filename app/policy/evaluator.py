def evaluate_condition(condition,facts):

    field_value = facts.get(condition.field)

    if field_value is None:
        return False

    if condition.operator == "==":
        return field_value == condition.value

    if condition.operator == "!=":
        return field_value != condition.value

    if condition.operator == ">":
        return field_value > condition.value

    if condition.operator == ">=":
        return field_value >= condition.value

    if condition.operator == "<":
        return field_value < condition.value

    if condition.operator == "<=":
        return field_value <= condition.value

    if condition.operator == "contains":
        return condition.value in field_value

    return False

def evaluate_rule(rule, facts):

    for condition in rule.conditions:

        if not evaluate_condition(condition, facts):
            return False

    return True

def find_matching_rules(rules, action, facts):

    matches = []

    for rule in rules:

        if rule.action != action:
            continue

        if evaluate_rule(rule, facts):
            matches.append(rule)

    matches.sort(
        key=lambda rule: rule.priority,
        reverse=True
    )

    return matches

    
 