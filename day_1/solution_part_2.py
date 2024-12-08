def solution(input_string: str) -> int:
    lines = input_string.strip().split('\n')
    list1, list2 = zip(*[map(int, line.split()) for line in lines])

    # Find similarity score
    similarity_score = sum([num * list2.count(num) for num in list1])
    return similarity_score
