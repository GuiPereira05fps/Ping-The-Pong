#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.Menu import Menu


class Game:

    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(900, 600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Checks events
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()
            #         quit()
