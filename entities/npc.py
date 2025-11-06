import pygame

npc_img = pygame.image.load('assets/mrs_willow.png').convert_alpha()

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.image = pygame.transform.scale(npc_img, (64, 96))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.name = name

    def get_dialogue(self, inventory):
        if 'yarn' not in inventory:
            return ['Oh hello, kitty!', 'Have you seen my Ball of Yarn?']
        else:
            return ['My yarn! Thank you sweet cat.', 'Here, a bow for you.']
