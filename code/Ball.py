#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.Const import WIN_HEIGHT, WIN_WIDTH


class Ball(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.player1 = None
        self.player2 = None
        self.speed_x = 6
        self.speed_y = 6

    def players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 12 or self.rect.bottom >= (WIN_HEIGHT - 12):
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= WIN_WIDTH:
            self.speed_x *= -1

        if self.rect.colliderect(self.player1) or self.rect.colliderect(self.player2):
            self.speed_x *= -1
