#!/usr/bin/python
# -*- coding: utf-8 -*-
from turtledemo import clock
from xml.dom.minidom import Entity

import pygame
from pygame import Font, Surface, Rect

from code.Ball import Ball
from code.EntityFactory import EntityFactory
from code.Const import PLAYERS_CENTERY, PLAYER1_X_AXIS, PLAYER2_X_AXIS, BALL_CENTER, WIN_WIDTH, LEVEL_SCREEN_CENTERY, \
    XAXIS_CENTER, YAXIS_CENTER


class Level:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("assets/level_BG.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        self.player1 = EntityFactory.get_entity("player1", (PLAYER1_X_AXIS, PLAYERS_CENTERY))
        self.player2 = EntityFactory.get_entity("player2", (PLAYER2_X_AXIS, PLAYERS_CENTERY))
        self.ball = EntityFactory.get_entity("ball", BALL_CENTER)
        self.ball.players(self.player1, self.player2)

        self.winner_soundeffect = pygame.mixer.Sound('assets/winner.wav')

    def run(self):
        pygame.mixer_music.load('assets/placeholder_Level_Soundtrack.mp3')
        pygame.mixer_music.set_volume(0.5)
        pygame.mixer_music.play(-1)
        fps = pygame.time.Clock()

        player1_score, player2_score = 0, 0
        waiting_serve = False
        winner = False
        winner_text = ""
        instructions = "Press ESC to return to the main menu or SPACE to play again"

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
                        if winner:
                            pygame.mixer_music.set_volume(0.5)
                            winner = False
                        self.ball.serve()
                        waiting_serve = False

            # Players can move before serving.
            # To be changed in future updates after release
            self.player1.move()
            self.player2.move()

            # Game score
            if not waiting_serve:
                self.ball.move()

                if self.ball.rect.left <= 0:
                    player2_score += 1
                    self.ball.restart()
                    waiting_serve = True

                elif self.ball.rect.right >= WIN_WIDTH:
                    player1_score += 1
                    self.ball.restart()
                    waiting_serve = True

            # Winning Condition + SoundEffect
            if player1_score == 5:
                self.winner_soundeffect.play()
                winner = True
                winner_text = "PLAYER 1 WINS!"
                pygame.mixer_music.set_volume(0)
                player1_score, player2_score = 0, 0
                self.ball.restart()
                waiting_serve = True

            elif player2_score == 5:
                self.winner_soundeffect.play()
                winner = True
                winner_text = "PLAYER 2 WINS!"
                pygame.mixer_music.set_volume(0)
                player1_score, player2_score = 0, 0
                self.ball.restart()
                waiting_serve = True

            # Graphic Components Display
            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(source=self.player1.surf, dest=self.player1.rect)
            self.window.blit(source=self.player2.surf, dest=self.player2.rect)
            self.window.blit(source=self.ball.surf, dest=self.ball.rect)
            self.text_writer(48,
                             str(player1_score),
                             (255, 255, 255),
                             None,
                             (380, 70))
            self.text_writer(48,
                             str(player2_score),
                             (255, 255, 255),
                             None,
                             (520, 70))

            if winner:
                self.text_writer(50,
                                 winner_text,
                                 (255, 255, 255),
                                 (0, 0, 0),
                                 (XAXIS_CENTER, YAXIS_CENTER))
                self.text_writer(28,
                                 instructions,
                                 (255, 255, 255),
                                 (0, 0, 0),
                                 (XAXIS_CENTER, 510))

            pygame.display.flip()

    def text_writer(self, text_size: int, text, text_color: tuple, text_bg_color, text_position: tuple):
        text_font: Font = pygame.font.Font('./assets/fonts/squares.ttf', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color, text_bg_color)
        text_rect: Rect = text_surface.get_rect(center=text_position)
        self.window.blit(source=text_surface, dest=text_rect)
