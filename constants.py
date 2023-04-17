WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 16
SCALE_FACTOR = 1
y_symbols = 17
x_symbols = 40
images_wall = {
    "top_left": [['images/Objects/Wall.png'], 0, 3],
    "top_right": [['images/Objects/Wall.png'], 2, 3],
    "top_bottom": [['images/Objects/Wall.png'], 0, 4],
    "bottom_left": [['images/Objects/Wall.png'], 0, 5],
    "bottom_right": [['images/Objects/Wall.png'], 2, 5],
    "left_right": [['images/Objects/Wall.png'], 1, 3],
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
