from Tile import Tile
from constants import TILE_SIZE, SCALE_FACTOR, map_img
from getTiles import getTiles
from utils import isTileAnimated, pos_wall


class Map:

    def __init__(self):
        self.tiles = []
        symbol_map = open('map.txt').readlines()
        symbol_map = [line.rstrip() for line in symbol_map]
        size = TILE_SIZE * SCALE_FACTOR
        for i in range(len(symbol_map)):
            self.tiles.append([])
            for j in range(len(symbol_map[i])):
                if symbol_map[i][j] == '#':
                    image_path, x, y = map_img[symbol_map[i][j]][pos_wall(j, i, symbol_map)]
                    self.tiles[i].append(Tile(j * size, i * size,
                                              getTiles(image_path, x, y),
                                              isTileAnimated(symbol_map[i][j])))
                else:
                    image_path, x, y = map_img[symbol_map[i][j]]
                    self.tiles[i].append(Tile(j * size, i * size,
                        getTiles(image_path, x, y),
                        isTileAnimated(symbol_map[i][j])))

    def display(self, screen):
        for line in self.tiles:
            for tile in line:
                tile.display(screen)
