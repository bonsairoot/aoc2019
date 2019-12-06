#/usr/bin/python3


class Tree():
    def __init__(self, root_id):
        self.root = Node(root_id)
        self.nodes = {root_id: self.root}

    def iterate_from_node(self, n):
        current = self.nodes[n]
        i = 0
        path = []
        while (current != self.root):
            i += 1
            current = self.nodes[current.parent]
            path.append(current.parent)

        return i, path[::-1]

    def add_node(self, n, parent=None):
        self.nodes[n] = Node(n, parent)


class Node():
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent


def main():
    tree = Tree("COM")
    with open("aoc06_input.txt") as f:
        for line in f.readlines():
            p, c = line.strip().split(")")
            tree.add_node(c, p)

    orbits = 0
    for node in tree.nodes:
        orbits += tree.iterate_from_node(node)[0]
    print(f"Part I: {orbits}")

    c1, p1 = tree.iterate_from_node("SAN")
    c2, p2 = tree.iterate_from_node("YOU")

    i = 0
    while p1[i] == p2[i]:
        i += 1

    distance = c1 - i + c2 - i + 2
    print(f"Part II: {distance}")


if __name__ == "__main__":
    main()
