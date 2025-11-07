import pygame

item_img = pygame.image.load('assets/sprites/yarn.png').convert_alpha()

class Item(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.image = pygame.transform.scale(item_img, (32, 32))
        self.rect = self.image.get_rect(midbottom=(x, y))
