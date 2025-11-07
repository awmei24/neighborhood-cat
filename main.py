import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Neighborhood Cat')

clock = pygame.time.Clock()

from systems.gamestate import GameState
from scenes.street import StreetScene

def main():
    game_state = GameState()
    current_scene = StreetScene(game_state, screen)

    while game_state.running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            current_scene.handle_event(event)

        current_scene.update(dt)
        current_scene.render()
        pygame.display.flip()

if __name__ == '__main__':
    main()