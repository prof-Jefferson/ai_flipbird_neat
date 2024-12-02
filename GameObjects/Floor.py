import os
import pygame
import config

class Floor:
    SPEED = 0.15  # Velocidade do movimento do piso
    CHUNKS = 3  # Número de segmentos do piso

    def __init__(self, y):
        self.floor_sprite = None
        self.chunk_width = 0
        self.y = y
        self._chunks = []

    def load_sprite(self):
        # Carrega a textura do piso e redimensiona
        self.floor_sprite = pygame.transform.scale2x(
            pygame.image.load(os.path.join(config.TEXTURES_DIR, "base.png")).convert_alpha()
        )
        self.chunk_width = self.floor_sprite.get_width()

        # Cria os segmentos do piso
        for x in range(self.CHUNKS):
            self._chunks.append([self.floor_sprite, x * self.chunk_width])

    def move(self):
        for i, chunk in enumerate(self._chunks):
            chunk[1] -= self.SPEED  # Move o segmento para a esquerda

            # Reposiciona o segmento se sair da tela
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
