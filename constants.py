from enum import Enum

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 16
SCALE_FACTOR = 1
IMG_SIZE = TILE_SIZE*SCALE_FACTOR
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

images_character = {
    "paladin": [['images/Commissions/Paladin.png'], 0, 0]
}
walk_bottom = [
     [['images/Commissions/Paladin.png'], 0, 0],
     [['images/Commissions/Paladin.png'], 0, 1],
     [['images/Commissions/Paladin.png'], 0, 2],
     [['images/Commissions/Paladin.png'], 0, 3]
 ]
walk_left = [
    [['images/Commissions/Paladin.png'], 1, 0],
    [['images/Commissions/Paladin.png'], 1, 1],
    [['images/Commissions/Paladin.png'], 1, 2],
    [['images/Commissions/Paladin.png'], 1, 3]
]
walk_right = [
    [['images/Commissions/Paladin.png'], 2, 0],
    [['images/Commissions/Paladin.png'], 2, 1],
    [['images/Commissions/Paladin.png'], 2, 2],
    [['images/Commissions/Paladin.png'], 2, 3]
]
walk_up = [
    [['images/Commissions/Paladin.png'], 3, 0],
    [['images/Commissions/Paladin.png'], 3, 1],
    [['images/Commissions/Paladin.png'], 3, 2],
    [['images/Commissions/Paladin.png'], 3, 3]
]

#  Enum используется для организации корректной работы с константами (часто использующиеся
#  переменные)
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

