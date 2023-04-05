from Tile import Tile
from constants import TILE_SIZE, SCALE_FACTOR, map_img
from utils import isTileAnimated


class Map:

    def __init__(self):
        self.tiles = []
        symbol_map = open('map1').readlines()
        size = TILE_SIZE * SCALE_FACTOR
        for i in range(len(symbol_map)):
            self.tiles.append([])
            for j in range(len(symbol_map[i])):
                self.tiles[i].append(Tile(j * size, i * size,
                                          map_img[symbol_map[i][j]],
                                          isTileAnimated(symbol_map[i][j])))

    def display(self, screen):
        for line in self.tiles:
            for tile in line:
                tile.display(screen)
