from constants import WINDOW_WIDTH, WINDOW_HEIGHT


def pos_check(x, y, size):
    dx = size - WINDOW_WIDTH
    dy = size - WINDOW_HEIGHT
    to_00 = [(0, 0), (dx, 0), (0, dy), (dx, dy),
             (dy, -x), (0, -x), (dy, -x), (0, -y), (dx, -y)]
    pos = 0
    for i, j in enumerate(to_00):
        x1 = x + j[0]
        y1 = y + j[1]
        if not (x1 and y1):
            pos = i
            break
    return pos
