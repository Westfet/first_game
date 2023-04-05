from Tile import Tile
from constants import TILE_SIZE, SCALE_FACTOR
from utils import getTiles


class Map:

    def __init__(self):
        self.tiles = []
        symbol_map = open('map1').readlines()
        images_wall = []
        image_floor = [getTiles(['images/Objects/Floor.png'], 1, 11)[0]]
        images_fire = [getTiles(['images/Objects/Effect0.png'], 1, 21)[0],
          getTiles(['images/Objects/Effect1.png'], 1, 21)[0]]
        for i in range(len(symbol_map)):
            symbol_map[i] = symbol_map[i].replace('\n', '')
        for i in range(3, 6):
            for j in range(3):
                images_wall.append(getTiles(['images/Objects/Wall.png'], j,
                                            i)[0])
        for i in range(len(symbol_map)):
            self.tiles.append([])
            for j in range(len(symbol_map[i])):
                if symbol_map[i][j] == '!':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              [images_wall[0]]))
                elif symbol_map[i][j] == '-':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              [images_wall[1]]))
                elif symbol_map[i][j] == '@':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              [images_wall[2]]))
                elif symbol_map[i][j] == '|':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              [images_wall[3]]))
                elif symbol_map[i][j] == '#':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              [images_wall[8]]))
                elif symbol_map[i][j] == '$':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              [images_wall[6]]))
                elif symbol_map[i][j] == ' ':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              image_floor))
                elif symbol_map[i][j] == '*':
                    self.tiles[i].append(Tile(j * TILE_SIZE * SCALE_FACTOR,
                                              i * TILE_SIZE * SCALE_FACTOR,
                                              images_fire, True))

    def display(self, screen):
        for line in self.tiles:
            for tile in line:
                tile.display(screen)
