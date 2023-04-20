from Tile import Tile
from constants import Direction


class Character(Tile):
    direction: Direction = None

    def __init__(self, hp, inventory, x, y, images, direction):
        super().__init__(x, y, images)
        self.hp = hp
        self.inventory = inventory
        self.direction = direction



