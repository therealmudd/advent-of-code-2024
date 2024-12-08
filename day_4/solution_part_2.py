def solution(input_string: str) -> int:
    puzzle = input_string.strip().split("\n")

    # Find the number of times an X-MAS appears
    indices = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
    
    x_mas_grid_rotations = [
        ['M.M', '.A.', 'S.S'], 
        ['S.M', '.A.', 'S.M'], 
        ['S.S', '.A.', 'M.M'], 
        ['M.S', '.A.', 'M.S']
    ]

    [print("\n".join(row), end="\n\n") for row in x_mas_grid_rotations]

    count = 0

    for i in range(len(puzzle) - 2):
        for j in range(len(puzzle[0]) - 2):
            subgrid = [row[j:j + 3] for row in puzzle[i:i + 3]]
            for rotation in x_mas_grid_rotations:
                if all(subgrid[i][j] == rotation[i][j] for i, j in indices):
                    count += 1
    return count
