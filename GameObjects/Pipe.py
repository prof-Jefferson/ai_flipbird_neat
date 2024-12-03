import os
import random
import pygame
import config

class Pipe:
    GAP_SIZE = 150  # Espaço entre os canos superior e inferior
    SPEED = 0.12    # Velocidade de movimento dos canos

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.UPPER_PIPE = None
        self.LOWER_PIPE = None
        self.passed = False  # Indica se o pássaro passou pelo cano

        self.load_pipe_sprites()
        self.set_pipe_height()

    def load_pipe_sprites(self):
        # Carrega as imagens dos canos
        pipe_sprite_path = os.path.join(config.TEXTURES_DIR, "pipe-green.png")
        self.pipe_sprite = pygame.image.load(pipe_sprite_path).convert_alpha()
        self.UPPER_PIPE = pygame.transform.flip(self.pipe_sprite, False, True)  # Inverte verticalmente
        self.LOWER_PIPE = self.pipe_sprite

    def set_pipe_height(self):
        # Define alturas aleatórias para os canos
        max_pipe_height = config.WINDOW_SIZE[1] - self.GAP_SIZE - 100  # Evita sobreposição
        self.height = random.randint(50, max_pipe_height)
        self.top = self.height - self.UPPER_PIPE.get_height()
        self.bottom = self.height + self.GAP_SIZE

    def move(self):
        # Move os canos para a esquerda
        self.x -= self.SPEED
    
    def collide(self, bird, screen=None):
        """
        Verifica se o centro do pássaro colidiu com este cano.
        :param bird: Objeto do tipo Bird.
        :param screen: (Opcional) Superfície para debug visual.
        :return: True se colidir, False caso contrário.
        """
        bird_center = bird.x + bird.cframe.get_width() // 2, bird.y + bird.cframe.get_height() // 2

        # Verifica colisão com o cano superior
        if self.x < bird_center[0] < self.x + self.UPPER_PIPE.get_width() and bird_center[1] < self.top + self.UPPER_PIPE.get_height():
            return True

        # Verifica colisão com o cano inferior
        if self.x < bird_center[0] < self.x + self.LOWER_PIPE.get_width() and bird_center[1] > self.bottom:
            return True

        return False

    def draw(self, screen):
        # Renderiza os canos na tela
        screen.blit(self.UPPER_PIPE, (self.x, self.top))
        screen.blit(self.LOWER_PIPE, (self.x, self.bottom))