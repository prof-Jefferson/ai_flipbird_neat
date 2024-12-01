import pygame

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (360, 640)  # Proporção de celular
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - Animação do Pássaro")

# Carregar as imagens para a animação
bird_frames = [
    pygame.image.load("textures/bird_black1.png"),
    pygame.image.load("textures/bird_black2.png"),
    pygame.image.load("textures/bird_black3.png")
]
bird_index = 0
bird_rect = bird_frames[0].get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))  # Centraliza o sprite

# Controle da animação
ANIMATION_SPEED = 210  # Velocidade da animação (frames por atualização)
frame_count = 0  # Contador para controlar o índice do sprite

# Loop do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a animação
    frame_count += 1
    if frame_count >= ANIMATION_SPEED:
        bird_index = (bird_index + 1) % len(bird_frames)  # Cicla entre os frames
        frame_count = 0

    # Atualizar a tela
    screen.fill((135, 206, 250))  # Cor de fundo (azul claro)
    screen.blit(bird_frames[bird_index], bird_rect.topleft)  # Desenha o frame atual
    pygame.display.update()

pygame.quit()