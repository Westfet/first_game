WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 16
SCALE_FACTOR = 1
map_rows = 19
images_wall = {
    "top_left": [['images/Objects/Wall.png'], 0, 3],
    "top_right": [['images/Objects/Wall.png'], 2, 3],
    "bottom_left": [['images/Objects/Wall.png'], 0, 5],
    "bottom_right": [['images/Objects/Wall.png'], 2, 5],
    "horizontal_bottom": [['images/Objects/Wall.png'], 1, 3],
    "horizontal_top": [['images/Objects/Wall.png'], 1, 3],
    "vertical_left": [['images/Objects/Wall.png'], 0, 4],
    "vertical_right": [['images/Objects/Wall.png'], 0, 4]
}

image_floor = [[['images/Objects/Floor.png'], 1, 11]]
images_fire = [[['images/Objects/Effect0.png', 'images/Objects/Effect1.png'],
               1, 21]]
map_img = {
    "#": list(images_wall.values()),
    " ": image_floor,
    "*": images_fire

}
animated_tiles = ["*"]
