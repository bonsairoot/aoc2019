#/usr/bin/python3
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


class Grid():
    def __init__(self):
        self.segments = []
        self.previous = Point(0, 0)
        self.current = Point(0, 0)

    def move(self, op):
        direction, steps = op[:1], int(op[1:])
        if direction == 'R':
            self.current = Point(self.previous.x + steps, self.previous.y)
        elif direction == 'L':
            self.current = Point(self.previous.x - steps, self.previous.y)
        elif direction == 'U':
            self.current = Point(self.previous.x, self.previous.y + steps)
        elif direction == 'D':
            self.current = Point(self.previous.x, self.previous.y - steps)

        self.segments.append((self.previous, self.current))
        self.previous = self.current

    def area(self, a, b, c):
        return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)

    def do_intersect(self, p1, q1, p2, q2):
        return self.area(p1, p2, q2) != self.area(q1, p2, q2) and self.area(p1, q1, p2) != self.area(p1, q1, q2)

    def intersections(self, grid2):
        assert (len(self.segments) == len(grid2.segments))
        intersections = []
        i = 0
        for p1, q1 in self.segments:
            i += abs(p1.x - q1.x) + abs(p1.y - q1.y)
            j = 0
            for p2, q2 in grid2.segments:
                j += abs(p2.x - q2.x) + abs(p2.y - q2.y)
                if self.do_intersect(p1, q1, p2, q2):
                    steps = i + j

                    # Assumes no colinearity (intersections are always orthogonal)
                    if p1.x == q1.x:
                        # Subtract paths from intersection to the end of the segments
                        steps -= abs(q1.y - p2.y) + abs(q2.x - p1.x)
                        intersection = Point(p1.x, p2.y)
                    else:
                        # Subtract paths from intersection to the end of the segments
                        steps -= abs(q1.x - p2.x) + abs(q2.y - p1.y)
                        intersection = Point(p1.y, p2.x)

                    intersections.append({
                        'intersection': intersection,
                        'steps': steps
                    })

        return intersections


def main():
    grids = []
    with open("aoc03_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            grids.append(Grid())
            for op in line.split(','):
                grids[i].move(op)

    intersections = grids[0].intersections(grids[1])
    min_dist = min([abs(p['intersection'].x) + abs(p['intersection'].y) for p in intersections])
    min_steps = min([p['steps'] for p in intersections])

    print(f"Part I: {min_dist}")
    print(f"Part II: {min_steps}")


if __name__ == "__main__":
    main()
