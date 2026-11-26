#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.examples.music_drop_fade import MUSIC_DONE

from code.Menu import Menu
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Level import Level


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Ping the Pong")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == 0:
                pygame.mixer.music.stop()
                level = Level(self.window)
                level_return = level.run()
                pass
            elif menu_return == 1:
                pass
            elif menu_return == 2:
                # Funny song played once game quits
                music_end_event = pygame.event.custom_type()
                pygame.mixer.music.set_endevent(music_end_event)
                pygame.mixer.music.load("./assets/quitting.mp3")
                pygame.mixer.music.play()

                playing = True
                while True:
                    for event in pygame.event.get():
                        if event.type == music_end_event:
                            pygame.quit()
                            quit()
