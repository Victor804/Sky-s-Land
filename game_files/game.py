import pygame
import os
from game_files.level import Level

class Game:
    def __init__(self):
        pygame.init()

        self.level = Level()

        self.display = pygame.display.set_mode((1920, 1000))

        background = pygame.image.load(os.getcwd()+"/game_files/images/background.jpeg")
        self.display.blit(background, (0,0))

        self.grass = pygame.image.load(os.getcwd()+"/game_files/images/grass.jpeg")

        pygame.display.flip()


    def maps_draw(self, stage=1):
        maps = self.level.load(stage)
        for i in maps:
            self.display.blit(self.grass, i)
