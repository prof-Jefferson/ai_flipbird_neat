import pygame

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (360, 640)  # Proporção de celular
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - Tela Principal")

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    screen.fill((135, 206, 250))  # Cor de fundo (azul claro)
    pygame.display.update()

pygame.quit()
