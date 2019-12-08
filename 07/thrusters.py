#/usr/bin/python3

import itertools
import operator


class Scanner():
    def __init__(self, inp):
        self.inp = inp
        self.address_to_store = -1
        self.head = 0
        self.tape = None
        self.last_out = 0

    def scan(self, instruction_input, persistent=False):
        tape = self.tape if self.tape else list(self.inp)
        head = self.head
        input_head = 0
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
                out = self.get_values(tape, params)[0]
                head += 2
                if persistent:
                    self.tape = tape
                    self.head = head
                self.last_out = out
                return out
            elif param_op == 3:
                tape[tape[head + 1]] = instruction_input[input_head]
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
                tape[tape[head + 3]] = int(values[0] < values[1])
                head += 4
            elif param_op == 8:
                tape[tape[head + 3]] = int(values[0] == values[1])
                head += 4
            else:
                raise RuntimeError("Invalid Opcode {},{}!".format(
                    param_op, op))
        return "DONE"

    def get_values(self, tape, params):
        values = []
        for param in params:
            if param[1]:
                values.append(param[0])
            else:
                values.append(tape[param[0]])
        return values


def main():
    with open('aoc07_input.txt') as f:
        inp = [int(x) for x in f.read().split(',')]

    scanner = Scanner(inp)
    t_values = {}
    for c in itertools.permutations(range(5)):
        t_in = 0
        for phase in c:
            t_in = scanner.scan([phase, t_in], False)
        t_values[t_in] = c

    print("Part I: {}".format(max(t_values.keys())))

    t_values = {}
    for c in itertools.permutations(range(5, 10)):
        t_in = 0
        scanners = [Scanner(inp) for x in c]
        loop_counter = 0
        while t_in != "DONE":
            for i, phase in enumerate(c):
                if loop_counter == 0:
                    t_in = scanners[i].scan([phase, t_in], True)
                else:
                    t_in = scanners[i].scan([t_in], True)
                if t_in == "DONE":
                    break
            loop_counter += 1
        t_values[scanners[-1].last_out] = c

    print("Part II: {}".format(max(t_values.keys())))


if __name__ == '__main__':
    main()
