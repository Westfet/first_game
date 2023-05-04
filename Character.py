from Tile import Tile
from constants import Direction


class Character(Tile):
    direction: Direction = None

    def __init__(self, hp, inventory, x, y, images, direction, is_animated):
        super().__init__(x, y, images, is_animated)
        self.hp = hp
        self.inventory = inventory
        self.direction = direction



