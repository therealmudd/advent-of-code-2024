def solution(input_string: str) -> None:
    equations = map(lambda x: x.replace(':', '').split(' '), input_string.strip().split("\n"))
    equations = list(map(lambda x: list(map(int, x)), equations))

    # Find the total calibration result
    total = 0

    for equation in equations:
        result, *values = equation
        if can_achieve(result, list(reversed(values))):
            total += result
        else:
            print(f"{equation[0]}: {' '.join(list(map(str, equation[1:])))}")

    return total

def can_achieve(result, values):
    if not values:
        return result == 0
    
    str_result = str(result)
    str_value = str(values[0])

    if len(str_result) == len(str_value) and str_result == str_value:
        return True

    if str_result[-len(str_value):] == str_value and \
    can_achieve(int(str_result[:-len(str_value)]), values[1:]):
        return True
    
    if result % values[0] == 0 and can_achieve(result // values[0], values[1:]):
        return True

    if result >= values[0] and can_achieve(result - values[0], values[1:]):
        return True
    
    return False