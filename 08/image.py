#/usr/bin/python3

from collections import Counter
from textwrap import wrap
from functools import reduce

W, H = (25, 6)


def sublayer_red(x, y):
    out = []
    for i in range(H):
        p = ""
        for pos in range(W):
            if x[i][pos] == '2':
                p += y[i][pos]
            else:
                p += x[i][pos]
        out.append(p)
    return out


def main():
    with open("aoc08_input.txt") as f:
        image = f.read().strip()
    layer_size = W * H
    layers = wrap(image, layer_size)
    counts = sorted([Counter(x) for x in layers], key=lambda x: x.get('0', 0))
    print("Part I: {}".format(counts[0]['1'] * counts[0]['2']))
    sublayers = [wrap(x, W) for x in layers]
    image_decoded = list(reduce(sublayer_red, sublayers))
    image_decoded = [x.replace('1', "\u25A0").replace('0', "\u25A1") for x in image_decoded]
    print("Part II: ")
    for line in image_decoded:
        print(line)


if __name__ == "__main__":
    main()
