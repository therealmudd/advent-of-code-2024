def solution(input_string: str) -> int:
    lines = input_string.strip().split('\n')
    list1, list2 = zip(*[map(int, line.split()) for line in lines])

    # Find total distance
    total_distance = sum([abs(a - b) for a, b in zip(sorted(list1), sorted(list2))])
    return total_distance
