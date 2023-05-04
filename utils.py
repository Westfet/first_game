from constants import animated_tiles, x_symbols, y_symbols


def isTileAnimated(x):
    return x in animated_tiles


def out(x, y, x_symbols, y_symbols):
    return x < 0 or x > x_symbols - 1 or y < 0 or y > y_symbols - 1


def pos_wall(x, y, array):
    around = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    pos_array = ["top", "bottom", "left", "right"]
    pos = []
    for i, j in enumerate(around):
        dx = x + j[0]
        dy = y + j[1]
        if not (out(dx, dy, x_symbols, y_symbols)):
            if array[dy][dx] == "#":
                pos.append(pos_array[i])
    if ('top' not in pos) and ('bottom' not in pos):
        return "horizontal"
    elif ('left' not in pos) and ('right' not in pos):
        return "vertical"
    else:
        return "_".join(pos)
