import pygame

class DialogueBox:
    def __init__(self, font):
        self.font = font
        self.active = False
        self.lines = []
        self.current_index = 0

    def start(self, lines):
        self.lines = lines
        self.current_index = 0
        self.active = True

    def advance(self):
        self.current_index += 1
        if self.current_index >= len(self.lines):
            self.active = False

    def render(self, surface):
        if not self.active:
            return
        WIDTH, HEIGHT = surface.get_size()
        text = self.lines[self.current_index]
        box = pygame.Rect(50, HEIGHT - 120, WIDTH - 100, 80)
        pygame.draw.rect(surface, (255, 255, 255), box, border_radius=8)
        pygame.draw.rect(surface, (50, 50, 50), box, 3, border_radius=8)
        rendered = self.font.render(text, True, (30, 30, 30))
        surface.blit(rendered, (box.x + 20, box.y + 25))
