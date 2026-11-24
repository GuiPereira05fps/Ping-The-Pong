#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity


class Player2(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        press_key = pygame.key.get_pressed()
        if press_key[pygame.K_UP] and self.rect.y > 18:
            self.rect.centery -= 25
        elif press_key[pygame.K_DOWN] and self.rect.y < 518:
            self.rect.centery += 25
        pass
