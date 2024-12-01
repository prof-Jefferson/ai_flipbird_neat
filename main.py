import pygame

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (360, 640)  # Proporção de celular
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - Olá Mundo!")

# Fonte para o texto
font = pygame.font.SysFont("Arial", 36)  # Usando a fonte Arial
text = font.render("Olá Mundo!", True, (0, 0, 0))  # Texto na cor preta
text_rect = text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))  # Centraliza o texto

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    screen.fill((135, 206, 250))  # Cor de fundo (azul claro)
    screen.blit(text, text_rect)  # Desenha o texto na tela
    pygame.display.update()

pygame.quit()
