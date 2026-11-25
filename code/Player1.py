#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity
from code.Const import WIN_HEIGHT


class Player1(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 8

    def move(self, ):
        press_key = pygame.key.get_pressed()
        if press_key[pygame.K_w]:
            self.rect.y = max(12, self.rect.y - self.speed)
        elif press_key[pygame.K_s]:
            bottom_limit = WIN_HEIGHT - 12 - self.rect.height
            self.rect.y = min(bottom_limit, self.rect.y + self.speed)
        pass
