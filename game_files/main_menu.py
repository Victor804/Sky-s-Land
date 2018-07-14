import pygame
import os
import numpy as np

class Menu:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((640, 480))
        self.x_start_button = 56
        self.y_start_button = 105

        self.x_saves_button = 156
        self.y_saves_button = 105

        self.x_options_button = 256
        self.y_options_button = 105

    def main(self):
        """
        Affichage du menu principal
        retourne play, saves, options
        """
        #Bouton pour lancer le jeu
        start_button = pygame.image.load(os.getcwd()+"/game_files/images/start.png")
        self.start_button_rect = start_button.get_rect()
        self.start_button_rect.x = self.x_start_button
        self.start_button_rect.y = self.y_start_button
        self.display.blit(start_button, (self.x_start_button,self.y_start_button))

        #Bouton pour gérer les sauvegarde
        saves_button = pygame.image.load(os.getcwd()+"/game_files/images/saves.png")
        self.saves_button_rect = saves_button.get_rect()
        self.saves_button_rect.x = self.x_saves_button
        self.saves_button_rect.y = self.y_saves_button
        self.display.blit(saves_button, (self.x_saves_button,self.y_saves_button))


        #Bouton pour gérer les options
        options_button = pygame.image.load(os.getcwd()+"/game_files/images/options.png")
        self.options_button_rect = options_button.get_rect()
        self.options_button_rect.x = self.x_options_button
        self.options_button_rect.y = self.y_options_button
        self.display.blit(options_button, (self.x_options_button,self.y_options_button))

        pygame.display.flip()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            x, y = pygame.mouse.get_pos()

            if (self.start_button_rect.collidepoint(x, y) and pygame.mouse.get_pressed()[0]):
                return "play"

            elif (self.saves_button_rect.collidepoint(x, y) and pygame.mouse.get_pressed()[0]):
                return "saves"

            elif (self.options_button_rect.collidepoint(x, y) and pygame.mouse.get_pressed()[0]):
                return "options"
