import pygame
import os

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (288, 512)  # Tamanho ajustado à imagem
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - IA")

# Carregar a imagem do fundo
bg_path = os.path.join("textures", "background-day.png")
bg_image = pygame.image.load(bg_path).convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    screen.blit(bg_image, (0, 0))  # A imagem cobre toda a tela
    pygame.display.update()

pygame.quit()
