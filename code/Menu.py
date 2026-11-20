#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import NEWGAME_BUTTON_YAXIS, CONTROLS_BUTTON_YAXIS, XAXIS_CENTER


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('assets/placeholder_BG_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load("./assets/placeholder_Menu_Song.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            title = self.load_menu_textimage(
                './assets/placeholder_title.png',
                XAXIS_CENTER,
                0)

            button_play = self.load_menu_textimage(
                './assets/placeholder_Menu_Buttons.jpg',
                XAXIS_CENTER,
                NEWGAME_BUTTON_YAXIS)

            button_controls = self.load_menu_textimage(
                './assets/placeholder_Menu_Buttons.jpg',
                XAXIS_CENTER,
                CONTROLS_BUTTON_YAXIS)

            # Checks events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    # Factory for menu text images
    def load_menu_textimage(self, image_path, center_x, y_axis):
        self.surf = pygame.image.load(image_path).convert_alpha()
        self.rect = self.surf.get_rect(centerx=center_x, top=y_axis)
        self.window.blit(source=self.surf, dest=self.rect)

        return self.surf, self.rect
