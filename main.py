import pygame
from Map import Map
from Ball import Ball
from Tile import Tile
from getTiles import getTiles

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# images = [getTiles(['images/Characters/Aquatic0.png'], 0, 3)[0],
#           getTiles(['images/Characters/Aquatic1.png'], 0, 3)[0]]
# tile = Tile(100, 100, images, True)
# character = Ball()
# characters = [Ball() for i in range(1000)]
game_map = Map()
running = True
while running:
    # screen.fill((0, 0, 0))
    # Отслеживание события: "закрыть окно"
    # модуль pygame.event используется для обработки очереди событий
    # pygame.event.get - получает события и очереди
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # tile.display(screen)
    # for character in characters:
    # character.change_coord()
    # character.display(screen)
    game_map.display(screen)
    pygame.display.update()
# завершение работы
pygame.quit()
