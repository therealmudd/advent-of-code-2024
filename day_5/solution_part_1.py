from collections import defaultdict

def solution(input_string: str) -> None:
    rules, all_updates = input_string.strip().split("\n\n")
    rules = rules.split("\n")
    all_updates = list(map(lambda x: x.split(","), all_updates.split("\n")))

    # Find the solution
    rules_dict = defaultdict(set)
    for rules in rules:
        a, b = rules.split("|")
        rules_dict[a].add(b)

    correcly_ordered = []

    for updates in all_updates:
        seen = set()
        for page in updates:
            if seen.intersection(rules_dict[page]) != set():
                break
            seen.add(page)
        else:
            correcly_ordered.append(updates)

    sum_of_middles = sum(int(updates[len(updates) // 2]) for updates in correcly_ordered)
    return sum_of_middles