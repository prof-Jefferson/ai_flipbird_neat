import os
import pygame
import config

class Floor:
    SPEED = 7  # Velocidade do movimento do piso
    CHUNKS = 3  # Número de segmentos do piso

    def __init__(self, y):
        self.floor_sprite = None
        self.chunk_width = 0
        self.y = y
        self._chunks = []

    def load_sprite(self):
        pass  # Este método será implementado na próxima etapa

    def move(self):
        pass  # Este método será implementado na próxima etapa

    def draw(self, screen):
        pass  # Este método será implementado na próxima etapa