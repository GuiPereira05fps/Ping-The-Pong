#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity
from code.Const import WIN_HEIGHT


class Player1(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self, ):
        press_key = pygame.key.get_pressed()
        if press_key[pygame.K_w] and self.rect.y > 18:
            self.rect.centery -= 25
        elif press_key[pygame.K_s] and self.rect.y < 518:
            self.rect.centery += 25
        pass
