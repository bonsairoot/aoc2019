#/usr/bin/python3

from constraint import *
from collections import Counter


def main():
    with open("aoc04_input.txt") as f:
        lb, ub = f.read().split('-')

    problem = Problem()
    for i in range(len(lb)):
        if i > 0:
            domain = range(min(domain), 10)
            problem.addVariable(i, domain)
            problem.addConstraint(lambda x, y: y > x or y == x, (i - 1, i))
        else:
            domain = range(int(lb[i]), int(ub[i]) + 1)
            problem.addVariable(i, domain)

    # Part I
    # problem.addConstraint(lambda u,v,w,x,y,z: u==v or v==w or w==x or x==y or y==z,range(6))

    # Part II
    problem.addConstraint(lambda *args: 2 in Counter(args).values(), range(6))

    in_bound_solutions = []
    for solution in problem.getSolutions():
        out = int(''.join([str(v) for k, v in sorted(solution.items())]))
        if out >= int(lb) and out <= int(ub):
            in_bound_solutions.append(out)

    print(len(in_bound_solutions))


if __name__ == "__main__":
    main()
