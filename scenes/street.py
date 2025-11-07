import pygame
from entities.cat import Cat
from entities.npc import NPC
from entities.item import Item
from systems.dialogue import DialogueBox

class StreetScene:
    def __init__(self, game_state, screen):
        self.game_state = game_state
        self.screen = screen
        self.WIDTH, self.HEIGHT = screen.get_size()

        # --- assets ---
        self.background = self.load_image('assets/backgrounds/street_bg.png', (self.WIDTH, self.HEIGHT))
        self.FONT = pygame.font.Font(None, 28)

        # --- entities ---
        self.cat = Cat(400, self.HEIGHT - 50)
        self.mrs_willow = NPC(650, self.HEIGHT - 50, 'Mrs. Willow')
        self.yarn_item = Item('yarn', 300, self.HEIGHT - 50)

        self.dialogue_box = DialogueBox(self.FONT)
        self.all_sprites = pygame.sprite.Group(self.cat, self.mrs_willow, self.yarn_item)

    def load_image(self, path, size=None):
        try:
            img = pygame.image.load(path).convert_alpha()
        except:
            img = pygame.Surface((50, 50))
            img.fill((180, 140, 120))
        if size:
            img = pygame.transform.scale(img, size)
        return img

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.dialogue_box.active:
                self.dialogue_box.advance()

            elif event.key == pygame.K_SPACE and not self.dialogue_box.active:
                if self.cat.rect.colliderect(self.mrs_willow.rect):
                    lines = self.mrs_willow.get_dialogue(self.game_state.inventory)
                    self.dialogue_box.start(lines)
                elif self.cat.rect.colliderect(self.yarn_item.rect):
                    self.game_state.inventory.append('yarn')
                    self.all_sprites.remove(self.yarn_item)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if not self.dialogue_box.active:
            self.cat.handle_input(keys)
        self.cat.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.dialogue_box.render(self.screen)

        inv_text = self.FONT.render(f'Inventory: {', '.join(self.game_state.inventory)}', True, (255, 255, 255))
        self.screen.blit(inv_text, (20, 20))
