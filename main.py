import pygame
from GameObjects.Background import Background
from GameObjects.Floor import Floor
from GameObjects.Bird import Bird
from GameObjects.Pipe import Pipe
import config

# Inicializar o Pygame
pygame.init()

# Configurações da janela
WINDOW_SIZE = config.WINDOW_SIZE  # Usar o tamanho definido no config.py
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird - IA")

# Inicializar objetos do jogo
background = Background()
background.load_sprite()

floor = Floor(y=400)
floor.load_sprite()

pipes = [Pipe(x=WINDOW_SIZE[0])]  # Inicializa um par de canos

bird = Bird(name="Flappy", color="red", x=50, y=256)
bird.load_frames()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird.jump()

    # Atualizar lógica do jogo
    bird.move()
    background.move()
    floor.move()

    # Atualizar e desenhar os canos
    for pipe in pipes:
        pipe.move()

    # Verificar colisão com o piso
    if bird.check_collision_with_floor(400):  # Y do piso
        print("Colisão com o piso!")
        running = False  # Encerrar o jogo ou reiniciar

    # Verificar colisão com os canos
    for pipe in pipes:
        if pipe.collide(bird, screen):  # Chama o método `collide` do Pipe
            print("Colisão com o cano!")
            running = False  # Encerrar o jogo ou reiniciar

    # Remover canos fora da tela
    if pipes and pipes[0].x < -pipes[0].UPPER_PIPE.get_width():
        pipes.pop(0)

    # Adicionar novos canos
    if len(pipes) == 0 or pipes[-1].x < WINDOW_SIZE[0] - config.PIPE_DISTANCE:
        pipes.append(Pipe(x=WINDOW_SIZE[0]))

    # Renderizar o fundo, piso, canos e pássaro
    screen.fill((135, 206, 250))  # Fundo azul claro
    background.draw(screen)
    floor.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
    bird.draw(screen)

    pygame.display.update()

pygame.quit()
