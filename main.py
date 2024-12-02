import pygame
from GameObjects.Background import Background
from GameObjects.Floor import Floor
from GameObjects.Bird import Bird

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (288, 512)  # Tamanho ajustado à imagem
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - IA")

# Inicializar o fundo e o piso
background = Background()
background.load_sprite()

floor = Floor(y=400)  # Altura ajustada para o piso
floor.load_sprite()

# Inicializar o pássaro
bird = Bird(name="Flappy", color="red", x=50, y=256)
bird.load_frames()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()    

    # Atualizar o fundo e o piso
    background.move()
    floor.move()
    bird.move()

    # Renderizar o fundo e o piso
    screen.fill((135, 206, 250))  # Fundo azul claro (para debug)
    background.draw(screen)  # Desenha o fundo animado
    floor.draw(screen)  # Desenha o piso animado
    bird.draw(screen)
    
    pygame.display.update()

pygame.quit()
