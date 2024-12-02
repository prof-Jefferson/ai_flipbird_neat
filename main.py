import pygame
import os
from GameObjects.Background import Background

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (288, 512)  # Tamanho ajustado à imagem
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - IA  ")

# Inicializar o fundo
background = Background()
background.load_sprite()

# Carregar manualmente a imagem do piso (temporário)
floor_path = os.path.join("textures", "base.png")
f_image = pygame.image.load(floor_path).convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar o fundo e o piso
    background.move()

    # Renderizar o fundo e o piso
    screen.fill((135, 206, 250))  # Fundo azul claro (se faltar algo, ajuda no debug)
    background.draw(screen)  # Desenha o fundo animado
    screen.blit(f_image, (0, 400))  # Desenha o piso fixo
    pygame.display.update()

pygame.quit()
