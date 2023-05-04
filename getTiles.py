import pygame
from constants import TILE_SIZE, SCALE_FACTOR, animated_tiles


def getTiles(paths, x, y):
    tiles = []
    for path in paths:
        image = pygame.image.load(path).convert().subsurface([
            # Передается 4 аргумента - две координаты + высота и ширина
            x * TILE_SIZE,
            y * TILE_SIZE,
            TILE_SIZE,
            TILE_SIZE,
        ])
        image = pygame.transform.scale(image, (TILE_SIZE * SCALE_FACTOR,
                                               TILE_SIZE * SCALE_FACTOR))
        tiles.append(image)
    return tiles


def isTileAnimated(x):
    return x in animated_tiles


# paths = [images_character["paladin"]]
# print(getTiles(paths, 0, 0))
