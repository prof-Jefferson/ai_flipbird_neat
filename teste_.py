import pygame
from GameObjects.Bird import Bird

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (288, 512)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Teste - Carregamento dos Frames do Pássaro")

# Inicializar o pássaro
bird = Bird(name="Teste", color="red", x=50, y=256)
bird.load_frames()  # Carregar os frames do pássaro

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Exibir o primeiro frame carregado na tela
    screen.fill((135, 206, 250))  # Fundo azul claro
    screen.blit(bird.frames[0], (bird.x, bird.y))  # Desenha o primeiro frame
    #bird.jump()
    pygame.display.update()    

pygame.quit()
