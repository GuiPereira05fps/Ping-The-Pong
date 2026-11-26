#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity
from code.Const import BOTTOM_BORDER_LIMITER, PLAYERS_SPEED


class Player2(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = PLAYERS_SPEED

    # Code duplication here and in Player1.
    # To be reviewed and updated in future versions after release.
    def move(self):
        press_key = pygame.key.get_pressed()
        if press_key[pygame.K_UP]:
            self.rect.y = max(12, self.rect.y - self.speed)
        elif press_key[pygame.K_DOWN]:
            bottom_limit = BOTTOM_BORDER_LIMITER - self.rect.height
            self.rect.y = min(bottom_limit, self.rect.y + self.speed)
        pass
