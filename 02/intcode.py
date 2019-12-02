#/usr/bin/python3

import itertools

def scan(inp, noun, verb):
    tape = list(inp)
    tape[1] = noun
    tape[2] = verb
    head = 0
    while tape[head] != 99:
        if tape[head] == 1:
            tape[tape[head + 3]] = tape[tape[head + 1]] + tape[tape[head + 2]]
        elif tape[head] == 2:
            tape[tape[head + 3]] = tape[tape[head + 1]] * tape[tape[head + 2]]
        else:
            raise RuntimeError("Invalid Opcode!")
        head += 4

    return tape[0]


def main():
    with open('aoc02_input.txt') as f:
        inp = [int(x) for x in f.read().split(',')]

    print("Part I: {}".format(scan(inp,12,2)))

    bound = range(100)
    for noun,verb in itertools.product(bound,bound):
        if scan(inp,noun,verb) == 19690720:
            print("Part II: {}".format(noun * 100 + verb))

if __name__ == '__main__':
    main()
