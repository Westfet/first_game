WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 16
SCALE_FACTOR = 1
y_symbols = 17
x_symbols = 40
images_wall = {
    "top_left": [['images/Objects/Wall.png'], 0, 3],
    "top_right": [['images/Objects/Wall.png'], 2, 3],
    "vertical": [['images/Objects/Wall.png'], 0, 4],
    "bottom_left": [['images/Objects/Wall.png'], 0, 5],
    "bottom_right": [['images/Objects/Wall.png'], 2, 5],
    "horizontal": [['images/Objects/Wall.png'], 1, 3],
    "top_bottom_left": [['images/Objects/Wall.png'], 3, 4],
    "top_bottom_right": [['images/Objects/Wall.png'], 5, 4],
    "top_left_right": [['images/Objects/Wall.png'], 4, 3],
    "bottom_left_right": [['images/Objects/Wall.png'], 4, 5],
    "top_bottom_left_right": [['images/Objects/Wall.png'], 4, 4]

}

image_floor = [['images/Objects/Floor.png'], 1, 11]
images_fire = [['images/Objects/Effect0.png', 'images/Objects/Effect1.png'],
               1, 21]
map_img = {
    "#": images_wall,
    " ": image_floor,
    "*": images_fire

}
animated_tiles = ["*"]
