import pygame
from constants import TILE_SIZE, SCALE_FACTOR


def getTiles(paths, x, y):
    tiles = []
    for path in paths:
        # pygame.image.load("путь к файлу") позволяет загрузить изображение и
        # возвращает объект Surface.
        # Метод .convert() используется для преобразования в pixel формат
        # Метод .subsurface() - создает поверхность для картинки на экране

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
