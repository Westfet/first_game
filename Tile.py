from getTiles import getTiles


class Tile:

    def __init__(self, x, y, images, is_animated=False):
        self.x = x
        self.y = y
        self.images = images
        self.is_animated = is_animated
        self.rect = self.images[0].get_rect(topleft=(self.x, self.y))
        self.animation_counter = 100

    def display(self, screen):
        if self.is_animated:
            self.animation_counter -= 1
            if not self.animation_counter:
                self.animation_counter = 100
            screen.blit(self.images[int(self.animation_counter > 50)],
                        self.rect)
        else:
            screen.blit(self.images[0], self.rect)
