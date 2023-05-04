import pygame
import pygame.event
from constants import TILE_SIZE
from getTiles import getTiles
from Character import Character


class PlayerCharacter(Character):
    def __init__(self, hp, inventory, x, y, images, direction, is_animated):
        super().__init__(hp, inventory, x, y, images, direction, is_animated)

    def move(self, event: pygame.event.Event):
        if event.key == pygame.K_DOWN:
            self.images.pop(0)
            self.y += TILE_SIZE
            for i in range(4):
                self.images.append(getTiles(['images/Commissions/Paladin.png'], i, 0)[0])
            self.rect = self.images[0].get_rect(topleft=(self.x, self.y))
        elif event.key == pygame.K_UP:
            self.images.pop(0)
            self.y -= TILE_SIZE
            for i in range(4):
                self.images.append(getTiles(['images/Commissions/Paladin.png'], i, 3)[0])
            self.rect = self.images[0].get_rect(topleft=(self.x, self.y))
        elif event.key == pygame.K_LEFT:
            self.images.pop(0)
            self.x -= TILE_SIZE
            for i in range(4):
                self.images.append(getTiles(['images/Commissions/Paladin.png'], i, 1)[0])
            self.rect = self.images[0].get_rect(topleft=(self.x, self.y))
        elif event.key == pygame.K_RIGHT:
            self.images.pop(0)
            self.x += TILE_SIZE
            for i in range(4):
                self.images.append(getTiles(['images/Commissions/Paladin.png'], i, 2)[0])
            self.rect = self.images[0].get_rect(topleft=(self.x, self.y))

    def stay(self):
        del self.images[0:len(self.images) - 1]

