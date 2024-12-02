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
        # Carrega a textura do piso e redimensiona
        self.floor_sprite = pygame.transform.scale2x(
            pygame.image.load(os.path.join(config.TEXTURES_DIR, "base.png")).convert_alpha()
        )
        self.chunk_width = self.floor_sprite.get_width()

        # Cria os segmentos do piso
        for x in range(self.CHUNKS):
            self._chunks.append([self.floor_sprite, x * self.chunk_width])


    def move(self):
        pass  # Este método será implementado na próxima etapa

    def draw(self, screen):
        pass  # Este método será implementado na próxima etapa