#/usr/bin/python3

import itertools
import operator


class Scanner():
    def __init__(self, inp):
        self.inp = inp
        self.address_to_store = -1

    def scan(self, instruction_input):
        tape = list(self.inp)
        head = 0
        while tape[head] != 99:
            op = tape[head]
            digits = [int(x) for x in str(op).zfill(5)]
            param_op = digits[-1]

            if param_op not in [3, 4]:
                params = zip(tape[head + 1:head + 3], digits[1:3][::-1])
                values = self.get_values(tape, params)

            if param_op == 1:
                tape[tape[head + 3]] = operator.add(*values)
                head += 4
            elif param_op == 2:
                tape[tape[head + 3]] = operator.mul(*values)
                head += 4
            elif param_op == 4:
                params = [(tape[head + 1], digits[2])]
                print("{}".format(*self.get_values(tape, params)))
                head += 2
            elif param_op == 3:
                tape[tape[head + 1]] = instruction_input
                head += 2
            elif param_op == 5:
                if values[0] != 0:
                    head = values[1]
                else:
                    head += 3
            elif param_op == 6:
                if values[0] == 0:
                    head = values[1]
                else:
                    head += 3
            elif param_op == 7:
                tape[tape[head + 3]] = int(values[0] < values[1])
                head += 4
            elif param_op == 8:
                tape[tape[head + 3]] = int(values[0] == values[1])
                head += 4
            else:
                raise RuntimeError("Invalid Opcode {},{}!".format(param_op, op))

    def get_values(self, tape, params):
        values = []
        for param in params:
            if param[1]:
                values.append(param[0])
            else:
                values.append(tape[param[0]])
        return values


def main():
    with open('aoc05_input.txt') as f:
        inp = [int(x) for x in f.read().split(',')]

    scanner = Scanner(inp)
    scanner.scan(5)


if __name__ == '__main__':
    main()
