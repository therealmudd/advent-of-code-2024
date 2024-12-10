def solution(input_string: str) -> None:
    puzzle_map = list(map(list, input_string.strip().split("\n")))
    puzzle_hei = len(puzzle_map)
    puzzle_wid = len(puzzle_map[0])

    # Find the number of distinct positions visited
    count = 0

    pos = [-1, -1]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_ = dirs[0]

    while pos[1] == -1:
        pos[0] += 1
        pos[1] = getIndex(puzzle_map[pos[0]], '^')

    puzzle_map[pos[0]][pos[1]] = 'X'

    while True:
        targ_pos = [pos[0] + dir_[0], pos[1] + dir_[1]]
        if not (0 <= targ_pos[0] < puzzle_hei and 0 <= targ_pos[1] < puzzle_wid):
            break

        if puzzle_map[targ_pos[0]][targ_pos[1]] == '#':
            dir_ = dirs[(dirs.index(dir_) + 1) % 4]
            continue
        
        pos = targ_pos
        puzzle_map[pos[0]][pos[1]] = 'X'

    count = sum([row.count('X') for row in puzzle_map])

    return count

def getIndex(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1