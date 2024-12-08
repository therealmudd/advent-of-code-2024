def solution(input_string: str) -> int:    
    data = [list(map(int, line.split())) for line in input_string.strip().split('\n')]

    # Find number of safe reports
    total_safe_reports = 0
    for report in data:
        prev_diff = None
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if (not 1 <= abs(diff) <= 3) or (prev_diff is not None and sign(diff) != sign(prev_diff)):           
                break
            else:
                prev_diff = diff
        else:
            total_safe_reports += 1

    return total_safe_reports

def sign(x):
    return 0 if x == 0 else 1 if x > 0 else -1
