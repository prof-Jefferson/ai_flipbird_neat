import pygame

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (360, 640)  # Proporção de celular
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - Sprite do Pássaro")

# Carregar o sprite do pássaro
bird_image = pygame.image.load("textures/bird_blue1.png")  # Certifique-se de usar o caminho correto
bird_rect = bird_image.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))  # Centraliza o sprite

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    screen.fill((135, 206, 250))  # Cor de fundo (azul claro)
    screen.blit(bird_image, bird_rect.topleft)  # Desenha o sprite na tela
    pygame.display.update()

pygame.quit()

