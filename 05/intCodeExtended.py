#/usr/bin/python3

import itertools

class Scanner():
    def __init__(self, inp):
        self.inp = inp
        self.address_to_store = -1

    def scan(self, noun, verb):
        tape = list(self.inp)
        if noun:
            tape[1] = noun
        if verb:
            tape[2] = verb
        head = 0
        while tape[head] != 99:
            op = tape[head]
            if op<10:
                self.handle_ops(tape,op,head)
            else:
                print(op)
                digits = [int(x) for x in str(op)]
                op = digits[-1:]
                self.handle_ops(tape,op,head)

            head += 2 if op == 2 or op == 4 else 4

    def handle_ops(self,tape,op,head):
        if op == 1:
            tape[tape[head + 3]] = tape[tape[head + 1]] + tape[tape[head + 2]]
        elif op == 2:
            tape[tape[head + 3]] = tape[tape[head + 1]] * tape[tape[head + 2]]
        elif op == 3:
            self.address_to_store = tape[head + 1]
        elif op == 4:
            out_value = tape[tape[head + 1]]


def main():
    with open('aoc05_input.txt') as f:
        inp = [int(x) for x in f.read().split(',')]

    scanner = Scanner(inp)
    print("Part I: {}".format(scanner.scan(12,2)))

if __name__ == '__main__':
    main()
