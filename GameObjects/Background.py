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
        # Carrega a imagem do fundo e ajusta para o tamanho necessário
        self.bg_sprite = pygame.transform.scale(
            pygame.image.load(os.path.join(config.TEXTURES_DIR, "background-day.png")).convert_alpha(),
            (288, 512)
        )
        self.chunk_width = self.bg_sprite.get_width()

        # Cria os segmentos do fundo
        for x in range(self.CHUNKS):
            self._chunks.append([self.bg_sprite, x * self.chunk_width])

    def move(self):
        pass  # Este método será implementado na próxima etapa

    def draw(self, screen):
        pass  # Este método será implementado na próxima etapa
