#/usr/bin/python3

def main():
    with open('aoc01_input.txt') as f:
        inp = f.read()

    raw_fuel = 0
    total_fuel = 0
    for line in inp.splitlines():
        mass = int(line)//3 -2
        raw_fuel += mass
        while mass > 0:
            total_fuel += mass
            mass = mass//3 - 2

    print(f"Part I: {raw_fuel}")
    print(f"Part II: {total_fuel}")


if __name__ == '__main__':
    main()
