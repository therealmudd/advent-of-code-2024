def solution(input_string: str) -> int:
    puzzle = input_string.strip().split("\n")

    # Find the number of times XMAS appears
    count = 0
    hei = len(puzzle)
    wid = len(puzzle[0])

    # Check horizontal lines
    for hor_line in puzzle:
        count += hor_line.count("XMAS")
        count += hor_line.count("SAMX")

    # Check vertical lines
    for j in range(wid):
        ver_line = "".join(puzzle[i][j] for i in range(hei))
        count += ver_line.count("XMAS")
        count += ver_line.count("SAMX")
    
    # Check top-left to bottom-right diagonals
    for i in range(hei):
        diagonal = "".join([puzzle[i + k][k] for k in range(min(hei - i, wid))])
        count += diagonal.count("XMAS")
        count += diagonal.count("SAMX")

    for j in range(1, wid):
        diagonal = "".join([puzzle[k][j + k] for k in range(min(hei, wid - j))])
        count += diagonal.count("XMAS")
        count += diagonal.count("SAMX")

    # Check bottom-left to top-right diagonals
    for i in range(hei):
        diagonal = "".join([puzzle[i - k][k] for k in range(min(i + 1, wid))])
        count += diagonal.count("XMAS")
        count += diagonal.count("SAMX")

    for j in range(1, wid):
        diagonal = "".join([puzzle[hei - 1 - k][j + k] for k in range(min(hei, wid - j))])
        count += diagonal.count("XMAS")
        count += diagonal.count("SAMX")

    return count
