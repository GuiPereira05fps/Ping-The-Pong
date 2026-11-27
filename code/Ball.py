#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Entity import Entity
from code.Const import WIN_HEIGHT, WIN_WIDTH, TOP_BORDER_LIMITER, BOTTOM_BORDER_LIMITER


class Ball(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.player1 = None
        self.player2 = None
        # Static speed resulting in the ball making the same bounces once in a while.
        # Acceleration to be added in future versions after release.
        self.speed_x = 7
        self.speed_y = 7

    # Simple maneuver to have ball and players collision working, but shouldn't be like this.
    # To be reviewed and updated in future versions after release
    def players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Debugs ball going through screen broder by teleporting it to border limit and
        # reversing its speed
        if self.rect.top < TOP_BORDER_LIMITER:
            self.rect.top = TOP_BORDER_LIMITER
            self.speed_y = abs(self.speed_y)
        elif self.rect.bottom > BOTTOM_BORDER_LIMITER:
            self.rect.bottom = BOTTOM_BORDER_LIMITER
            self.speed_y = -abs(self.speed_y)

        # Players collisions mechanic
        # Absolute values ensure ball is always going to the opposite direction and solves
        # ball going through player glitch
        if self.rect.colliderect(self.player1.rect):
            self.speed_x = abs(self.speed_x)
        elif self.rect.colliderect(self.player2.rect):
            self.speed_x = -abs(self.speed_x)

    def restart(self):
        self.rect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)
        self.speed_x = 0
        self.speed_y = 0

    def serve(self):
        self.speed_x = random.choice([-7, 7])
        self.speed_y = random.choice([-7, 7])
