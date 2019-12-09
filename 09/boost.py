#/usr/bin/python3

import itertools
import operator
from collections import defaultdict

class Scanner():
    def __init__(self, inp):
        self.inp = inp
        self.head = 0
        self.tape = None
        self.last_out = 0
        self.done = False
        self.relative_base = 0

    def scan(self, instruction_input, persistent=False, stop_on_out=True):
        d = dict(x for x in enumerate(list(self.inp)))
        tape = self.tape if self.tape else defaultdict(lambda: 0, d)
        head = self.head
        input_head = 0
        while tape[head] != 99:
            op = tape[head]
            digits = [int(x) for x in str(op).zfill(5)]
            param_op = digits[-1]

            if param_op not in [3,4,9]:
                params = zip([tape[x] for x in tape if x>head and x < head+3], digits[1:3][::-1])
                values = self.get_values(tape, params)
            elif param_op in [4,9]:
                params = [(tape[head + 1], digits[2])]
                values = self.get_values(tape, params)


            if param_op == 1:
                addr = self.get_addr(tape,(tape[head+3],digits[0]))
                tape[addr] = values[0] + values[1]
                head += 4
            elif param_op == 2:
                addr = self.get_addr(tape,(tape[head+3],digits[0]))
                tape[addr] = values[0] * values[1]
                head += 4
            elif param_op == 4:
                out = values[0]
                head += 2
                if persistent:
                    self.tape = tape
                    self.head = head
                self.last_out = out
                if stop_on_out:
                    return out
                else:
                    print(out)
            elif param_op == 3:
                addr = self.get_addr(tape,(tape[head+1],digits[2]))
                tape[addr] = instruction_input[input_head]
                input_head += 1
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
                addr = self.get_addr(tape,(tape[head+3],digits[0]))
                tape[addr] = int(values[0] < values[1])
                head += 4
            elif param_op == 8:
                addr = self.get_addr(tape,(tape[head+3],digits[0]))
                tape[addr] = int(values[0] == values[1])
                head += 4
            elif param_op == 9:
                self.relative_base += values[0]
                head += 2
            else:
                raise RuntimeError("Invalid Opcode {},{}!".format(
                    param_op, op))
        self.done = True

    def get_values(self, tape, params):
        values = []
        for param in params:
            if param[1] == 1:
                values.append(param[0])
            elif param[1] == 2:
                values.append(tape[param[0] + self.relative_base])
            else:
                values.append(tape[param[0]])
        return values

    def get_addr(self, tape, param):
        if param[1] == 2:
            return param[0] + self.relative_base
        else:
            return param[0]


def main():
    with open('aoc09_input.txt') as f:
        inp = [int(x) for x in f.read().split(',')]

    scanner = Scanner(inp)
    scanner.scan([2], stop_on_out = False)


if __name__ == '__main__':
    main()
