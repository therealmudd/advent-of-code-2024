import math

def solution(input_string: str) -> None:
    puzzle_map = list(map(list, input_string.strip().split("\n")))
    puzzle_hei = len(puzzle_map)
    puzzle_wid = len(puzzle_map[0])

    # Find the number of unique locations for antinodes
    antinodes = set()
    points = [Point(int(i), int(j), c) for i in range(puzzle_hei) for j, c in enumerate(puzzle_map[i]) if c != '.']

    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if j >= i or p1.value != p2.value:
                continue

            ang = math.atan2(p2.j - p1.j, p2.i - p1.i)
            dist = math.dist([p1.i, p1.j], [p2.i, p2.j])

            a1 = Point(p1.i - dist * math.cos(ang), p1.j - dist * math.sin(ang), '#')
            a2 = Point(p2.i + dist * math.cos(ang), p2.j + dist * math.sin(ang), '#')

            for a in [a1, a2]:
                if a.is_on_map(puzzle_hei, puzzle_wid):
                    antinodes.add(a)

    return len(antinodes)

class Point:
    def __init__(self, i, j, value="#"):
        self.i = round(i)
        self.j = round(j)
        self.value = value

    def is_on_map(self, puzzle_hei, puzzle_wid):
        return 0 <= self.i < puzzle_hei and 0 <= self.j < puzzle_wid

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.i, self.j, self.value) == (other.i, other.j, other.value)
        return False

    def __hash__(self):
        return hash((self.i, self.j, self.value))
    
    def __str__(self):
        return f"({self.i}, {self.j}, {self.value})"