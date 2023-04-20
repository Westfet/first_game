import pygame.event
from constants import TILE_SIZE

from Character import Character


class PlayerCharacter(Character):
    def __init__(self, hp, inventory, x, y, images, direction):
        super().__init__(hp, inventory, x, y, images, direction)

    def move(self, event: pygame.event.Event):
        if event.key == pygame.K_w:
            self.y = self.y - TILE_SIZE
            self.images = getTiles()