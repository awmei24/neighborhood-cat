import pygame

cat_img = pygame.image.load('assets/cat.png').convert_alpha()

class Cat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(cat_img, (64, 64))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = 4
        self.vel_y = 0
        self.gravity = 0.8
        self.on_ground = False

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = -12
            self.on_ground = False

    def update(self):
        # gravity + simple ground collision
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        if self.rect.bottom >= 550:
            self.rect.bottom = 550
            self.vel_y = 0
            self.on_ground = True
