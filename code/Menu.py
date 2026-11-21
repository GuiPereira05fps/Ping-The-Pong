#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import (
    MENU_NEWGAME_BUTTON_YAXIS,
    MENU_CONTROLS_BUTTON_YAXIS,
    MENU_EXIT_BUTTON_YAXIS,
    XAXIS_CENTER)


class Menu:
    # Set menu background image
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('assets/placeholder_BG_Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    # Play and loop soundtrack
    def run(self):
        selected_option = 0
        pygame.mixer_music.load("./assets/placeholder_Menu_Song.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            title = self.load_menu_textimage(
                './assets/placeholder_title.png',
                XAXIS_CENTER,
                5)

            newgame_path = (
                './assets/menu_button_NewGameHL.png' if selected_option == 0
                else './assets/menu_button_NewGame.png'
            )

            button_newgame = self.load_menu_textimage(
                newgame_path,
                XAXIS_CENTER,
                MENU_NEWGAME_BUTTON_YAXIS)

            controls_path = (
                './assets/menu_button_ControlsHL.png' if selected_option == 1
                else './assets/menu_button_Controls.png'
            )

            button_controls = self.load_menu_textimage(
                controls_path,
                XAXIS_CENTER,
                MENU_CONTROLS_BUTTON_YAXIS)

            quit_path = (
                './assets/menu_button_QuitHL.png' if selected_option == 2
                else './assets/menu_button_Quit.png'
            )

            button_quit = self.load_menu_textimage(
                quit_path,
                XAXIS_CENTER,
                MENU_EXIT_BUTTON_YAXIS)

            pygame.display.flip()

            # Checks events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % 3
                    elif event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % 3
                    elif event.key == pygame.K_RETURN:
                        return selected_option

    # Factory for menu text images
    def load_menu_textimage(self, image_path, center_x, y_axis):
        self.surf = pygame.image.load(image_path).convert_alpha()
        self.rect = self.surf.get_rect(centerx=center_x, top=y_axis)
        self.window.blit(source=self.surf, dest=self.rect)

        return self.surf, self.rect
