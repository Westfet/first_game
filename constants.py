from getTiles import getTiles

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 16
SCALE_FACTOR = 1
images_wall = {
    "top_left": getTiles(['images/Objects/Wall.png'], 0, 3)[0],
    "horizontal": getTiles(['images/Objects/Wall.png'], 1, 3)[0],
    "top_right": getTiles(['images/Objects/Wall.png'], 2, 3)[0],
    "vertical": getTiles(['images/Objects/Wall.png'], 0, 4)[0],
    "bottom_left": getTiles(['images/Objects/Wall.png'], 0, 5)[0],
    "bottom_right": getTiles(['images/Objects/Wall.png'], 2, 5)[0]
}
map_img = {
    "!": images_wall["top_left"],
    "-": images_wall["horizontal"],
    "@": images_wall["top_right"],
    "#": images_wall["bottom_right"],
    "$": images_wall["bottom_left"],
    " ": getTiles(['images/Objects/Floor.png'], 1, 11)[0],
    "*": getTiles(['images/Objects/Effect0.png'], 1, 21)[0] + \
         getTiles(['images/Objects/Effect1.png'], 1, 21)[0],
    "|": images_wall["vertical"]
}
animated_tiles = ["*"]
