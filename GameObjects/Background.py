import os
import pygame
import config

class Background:
    SPEED = 0.09  # Velocidade do movimento do fundo
    CHUNKS = 3   # Número de segmentos do fundo visíveis

    def __init__(self):
        self.bg_sprite = None
        self.chunk_width = 0
        self.y = 0
        self._chunks = []

    def load_sprite(self):
        try:
            self.bg_sprite = pygame.transform.scale(
                pygame.image.load(os.path.join(config.TEXTURES_DIR, "background-day.png")).convert_alpha(),
                (288, 512)
            )
        except FileNotFoundError:
            print("Erro: Arquivo 'background-day.png' não encontrado no diretório de texturas.")
            raise

        self.chunk_width = self.bg_sprite.get_width()

        # Cria os segmentos do fundo
        for x in range(self.CHUNKS):
            self._chunks.append([self.bg_sprite, x * self.chunk_width])

    def move(self, speed=None):
        actual_speed = speed if speed is not None else self.SPEED
        for i, chunk in enumerate(self._chunks):
            chunk[1] -= actual_speed
            if chunk[1] < -self.chunk_width:
                chunk[1] = self.get_last_chunk_offset() + self.chunk_width

    def get_last_chunk_offset(self):
        offset = 0
        for chunk in self._chunks:
            if chunk[1] > offset:
                offset = chunk[1]
        return offset

    def draw(self, screen):
        for chunk in self._chunks:
            screen.blit(chunk[0], (chunk[1], self.y))
