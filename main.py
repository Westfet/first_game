import pygame
from Map import Map
from getTiles import getTiles
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, images_character
from PlayerCharacter import PlayerCharacter

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game_map = Map()
player = PlayerCharacter(100, None, 16, 16, getTiles(*images_character["paladin"]), None, False)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.move(event)
        if event.type == pygame.KEYUP:
            player.stay()
    pygame.display.update()
    game_map.display(screen)
    player.display(screen)
pygame.quit()
