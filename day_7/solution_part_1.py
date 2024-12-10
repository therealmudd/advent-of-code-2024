def solution(input_string: str) -> None:
    equations = map(lambda x: x.replace(':', '').split(' '), input_string.strip().split("\n"))
    equations = list(map(lambda x: list(map(int, x)), equations))

    # Find the total calibration result
    total = 0

    for equation in equations:
        result, *values = equation
        if can_achieve(result, list(reversed(values))):
            total += result

    return total

def can_achieve(result, values):
    if not values:
        return result == 0
    
    if result % values[0] == 0 and can_achieve(result // values[0], values[1:]):
        return True

    if can_achieve(result - values[0], values[1:]):
        return True
    
    return False