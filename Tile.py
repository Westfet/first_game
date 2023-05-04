
class Tile:

    def __init__(self, x, y, images, is_animated=False):
        self.x = x
        self.y = y
        self.images = images
        self.is_animated = is_animated
        self.rect = self.images[0].get_rect(topleft=(self.x, self.y))
        self.animation_counter = 0

    def display(self, screen):
        if self.is_animated:
            fps = 30
            self.animation_counter += 1
            screen.blit(self.images[self.animation_counter // fps], self.rect)
            if self.animation_counter == (len(self.images) * fps) - 1:
                self.animation_counter = 0
        else:
            screen.blit(self.images[0], self.rect)

