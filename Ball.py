from utils import getTiles
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, TILE_SIZE


# import pygame.image


class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_direction = 1
        self.y_direction = 0
        self.counter = 1
        # 0,3 - позиция изображения на общей картинке
        # getTiles возвращает массив, нам нужен только 1-й элемент [0]
        self.image = getTiles(['images/Characters/Aquatic0.png'], 0, 3)[0]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def display(self, screen):
        # метод .blit() накладывает на родительскую поверхность - screen
        # дочернюю - image
        # (на вход принимает картинку + координаты левого верхнего угла)
        screen.blit(self.image, self.rect)

    def change_coord(self):
        self.x += self.x_direction
        self.y += self.y_direction
        if self.x == WINDOW_WIDTH - TILE_SIZE * self.counter:
            self.x_direction = 0
            self.y_direction = 1
        if self.y == WINDOW_HEIGHT - TILE_SIZE * self.counter:
            self.y_direction = 0
            self.x_direction = -1
        if self.x == TILE_SIZE * (self.counter - 1) and \
                self.y == WINDOW_HEIGHT - TILE_SIZE * self.counter:
            self.y_direction = -1
            self.x_direction = 0
        if self.y == TILE_SIZE * (self.counter - 1) and \
                self.x == TILE_SIZE * (self.counter - 1):
            self.x_direction = 1
            self.y_direction = 0
            self.counter += 1
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

