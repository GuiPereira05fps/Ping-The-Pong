#!/usr/bin/python
# -*- coding: utf-8 -*-
from turtledemo import clock
from xml.dom.minidom import Entity

import pygame

from code.Ball import Ball
from code.EntityFactory import EntityFactory
from code.Const import PLAYERS_CENTERY, PLAYER1_X_AXIS, PLAYER2_X_AXIS, BALL_CENTER, WIN_WIDTH


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
        player1_score = 0
        player2_score = 0
        waiting_serve = False
        pygame.mixer_music.load('assets/placeholder_Level_Soundtrack.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        fps = pygame.time.Clock()

        while True:
            fps.tick(60)

            # Checks events
            # It MUST be in this order and in the beginning of the loop.
            # Serving mechanic is verified here
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Quits level by pressing Escape key
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

                    if waiting_serve and event.key == pygame.K_SPACE:
                        self.ball.serve()
                        waiting_serve = False

            # Players can move before serving.
            # To be changed in future updates after release
            self.player1.move()
            self.player2.move()

            if not waiting_serve:
                self.ball.move()

                if self.ball.rect.left <= 0:
                    print("SCORE!")
                    player2_score += 1
                    print("\n\tPLAYER 1: ", player1_score, "\n\tPLAYER 2: ", player2_score)
                    self.ball.restart()
                    waiting_serve = True

                elif self.ball.rect.right >= WIN_WIDTH:
                    print("SCORE!")
                    player1_score += 1
                    print("\n\tPLAYER 1: ", player1_score, "\n\tPLAYER 2: ", player2_score)
                    self.ball.restart()
                    waiting_serve = True

            if player1_score == 5:
                print("\n\tPLAYER 1 WINS!")
                player1_score, player2_score = 0, 0
                self.ball.restart()
                waiting_serve = True

            elif player2_score == 5:
                print("\n\tPLAYER 2 WINS!")
                player1_score, player2_score = 0, 0
                self.ball.restart()
                waiting_serve = True

            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(source=self.player1.surf, dest=self.player1.rect)
            self.window.blit(source=self.player2.surf, dest=self.player2.rect)
            self.window.blit(source=self.ball.surf, dest=self.ball.rect)

            pygame.display.flip()
