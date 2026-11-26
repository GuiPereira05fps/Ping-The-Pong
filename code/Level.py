#!/usr/bin/python
# -*- coding: utf-8 -*-
from turtledemo import clock
from xml.dom.minidom import Entity

import pygame

from code.EntityFactory import EntityFactory
from code.Const import PLAYERS_CENTERY, PLAYER1_X_AXIS, PLAYER2_X_AXIS, BALL_CENTER


class Level:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("assets/level_BG.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        self.player1 = EntityFactory.get_entity("player1", (PLAYER1_X_AXIS, PLAYERS_CENTERY))
        self.player2 = EntityFactory.get_entity("player2", (PLAYER2_X_AXIS, PLAYERS_CENTERY))
        self.ball = EntityFactory.get_entity("ball", BALL_CENTER)

        self.ball.players(self.player1, self.player2)

    def run(self):
        pygame.mixer_music.load('assets/placeholder_Level_Soundtrack.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        fps = pygame.time.Clock()

        while True:
            fps.tick(60)
            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(source=self.player1.surf, dest=self.player1.rect)
            self.player1.move()
            self.window.blit(source=self.player2.surf, dest=self.player2.rect)
            self.player2.move()
            self.window.blit(source=self.ball.surf, dest=self.ball.rect)
            self.ball.move()

            pygame.display.flip()

            # Checks events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Quits level by pressing Escape key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
