import pygame
import os

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1920, 1080))

        background = pygame.image.load(os.getcwd()+"/game_files/images/background.jpeg")
        self.display.blit(background, (0,0))
        while True:
            pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(60)
