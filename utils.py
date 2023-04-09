from constants import animated_tiles, map_rows, WINDOW_WIDTH


def isTileAnimated(x):
    return x in animated_tiles


def pos_wall(x, y, size):
    dx = size - WINDOW_WIDTH
    dy = size - map_rows * size
    to_00 = [[0, 0], [dx, 0], [0, dy], [dx, dy],
             [-x, dy], [-x, 0], [0, -y], [dx, -y]]
    pos = 0
    for i, j in enumerate(to_00):
        x1 = x + j[0]
        y1 = y + j[1]
        if x1 == 0 and y1 == 0:
            pos = i
            break
    return pos
