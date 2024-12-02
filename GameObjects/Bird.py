import os
import random
import pygame
import config

class Bird:
    ROTATION_MAX_ANGLE = 25
    ROTATION_SPEED = 20
    GRAVITY = 0.0006
    FLAP_POWER = -0.25
    AVAILABLE_COLORS = ("blue", "red", "yellow", "purple", "toxic", "green", "teal", "pink", "white", "black", "orange")

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color if color in self.AVAILABLE_COLORS else random.choice(self.AVAILABLE_COLORS)
        self.x = x
        self.y = y
        self.angle = 0
        self.velocity = 0
        self.height = self.y
        self.frames = None
        self.cframe = None

    def load_frames(self):
        # Carrega os três frames para a animação do pássaro
        self.frames = [
            pygame.image.load(os.path.join(config.TEXTURES_DIR, f"bird_{self.color}{i}.png")).convert_alpha()
            for i in range(1, 4)
        ]
        self.cframe = self.frames[0]  # Define o frame inicial

    def move(self):
        self.velocity += self.GRAVITY
        self.y += self.velocity

        # Limita a velocidade de queda
        if self.velocity >= .6:
            self.velocity = .6

        # Atualiza o ângulo de acordo com o movimento
        if self.velocity < 0 or self.y < self.height + 50:
            if self.angle < self.ROTATION_MAX_ANGLE:
                self.angle = self.ROTATION_MAX_ANGLE
        else:
            if self.angle > -45:
                self.angle -= self.ROTATION_SPEED
    
    def jump(self):
        self.velocity = self.FLAP_POWER
        self.height = self.y

    def draw(self, screen):
        # Alterna entre os frames para animar
        self.cframe = self.frames[(pygame.time.get_ticks() // 200) % len(self.frames)]
        rotated_sprite = pygame.transform.rotate(self.cframe, self.angle)
        rect = rotated_sprite.get_rect(center=(self.x, self.y))
        screen.blit(rotated_sprite, rect.topleft)