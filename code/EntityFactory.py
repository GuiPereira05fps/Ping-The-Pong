#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Entity

import pygame
from code.Player1 import Player1
from code.Player2 import Player2


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case "player1":
                return Player1('player1', position)
            case "player2":
                return Player2('player2', position)
        return None
