def solution(input_string: str) -> int:    
    data = [list(map(int, line.split())) for line in input_string.strip().split('\n')]

    # Find number of safe reports
    total_safe_reports = 0
    for report in data:
        is_safe, point_of_failure = check_safety(report)
        if is_safe or check_safety(remove_at_index(report, point_of_failure))[0]:
            total_safe_reports += 1

    return total_safe_reports


def sign(x):
    return 0 if x == 0 else 1 if x > 0 else -1

def check_safety(report):
    diffs = [report[i] - report[i-1] for i in range(1, len(report))]
    ranges = [1 <= abs(diff) <= 3 for diff in diffs]
    signs = [sign(diff) for diff in diffs]

    for i, in_range in enumerate(ranges):
        if not in_range:
            return False, i

    first_sign = signs[0]
    for i in range(1, len(signs) - 1):
        if signs[i] != first_sign:
            return False, i

    is_safe = True
    point_of_failure = None
    return is_safe, point_of_failure


def remove_at_index(lst, i):
    return lst[:i] + lst[i+1:]
