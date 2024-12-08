import re

def solution(input_string: str) -> int:
    string = input_string.replace("\n", "x")
    
    # Find the sum of the multiplications
    result = 0
    min_length = len("(x,y)")
    max_length = len("(xxx,yyy)")
    pattern = "^\(\d{1,3},\d{1,3}\)$"

    for substring in string.split("mul"):
        length = len(substring)
        if min_length <= length:
            for i in range(min(length, max_length), min_length - 1, -1):
                sub_substring = substring[:i]
                if re.match(pattern, sub_substring):
                    print(sub_substring[1:-1])
                    x, y = map(int, sub_substring[1:-1].split(","))
                    result += x * y
    
    return result
