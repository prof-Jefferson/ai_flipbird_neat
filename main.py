import pygame
from GameObjects.Background import Background
from GameObjects.Floor import Floor
from GameObjects.Bird import Bird
from GameObjects.Pipe import Pipe
import config

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = (288, 512)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - IA")

# Inicializar elementos do jogo
background = Background()
background.load_sprite()

floor = Floor(y=400)
floor.load_sprite()

bird = Bird(name="Flappy", color="red", x=50, y=256)
bird.load_frames()

pipes = [Pipe(x=WINDOW_SIZE[0])]  # Inicializa um par de canos

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()

    # Atualizar elementos
    bird.move()
    background.move()
    floor.move()

    for pipe in pipes:
        pipe.move()

    # Adicionar novos canos se necessário
    if len(pipes) == 0 or pipes[-1].x < WINDOW_SIZE[0] - 200:
        pipes.append(Pipe(x=WINDOW_SIZE[0]))

    # Remover canos fora da tela
    if pipes and pipes[0].x < -pipes[0].UPPER_PIPE.get_width():
        pipes.pop(0)

    # Renderizar elementos
    screen.fill((135, 206, 250))
    background.draw(screen)
    floor.draw(screen)

    for pipe in pipes:
        pipe.draw(screen)

    bird.draw(screen)
    pygame.display.update()

pygame.quit()
