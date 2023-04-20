import pygame
from Map import Map
from getTiles import getTiles
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, images_character, Direction
from PlayerCharacter import PlayerCharacter

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game_map = Map()
player = PlayerCharacter(100, None, 0, 0, getTiles(images_character["player_character"]), None)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.move(event)
    game_map.display(screen)
    pygame.display.update()
pygame.quit()
