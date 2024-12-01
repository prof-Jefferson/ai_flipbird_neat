import os
import pygame
import config

class Background:
    SPEED = 0.5  # Velocidade do movimento do fundo
    CHUNKS = 4   # Número de segmentos do fundo visíveis

    def __init__(self):
        self.bg_sprite = None
        self.chunk_width = 0
        self.y = 0
        self._chunks = []

    def load_sprite(self):
        pass  # Este método será implementado na próxima etapa

    def move(self):
        pass  # Este método será implementado na próxima etapa

    def draw(self, screen):
        pass  # Este método será implementado na próxima etapa
