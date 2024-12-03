import pygame
from GameObjects.Bird import Bird
from GameObjects.Pipe import Pipe
from GameObjects.Floor import Floor
from GameObjects.Background import Background
import config


def run_game():
    pygame.init()

    # Configuração da janela
    screen = pygame.display.set_mode(config.WINDOW_SIZE)
    pygame.display.set_caption("Flappy Bird - Jogador")

    # Inicializar objetos do jogo
    background = Background()
    floor = Floor(y=400)
    pipes = [Pipe(x=config.WINDOW_SIZE[0])]
    bird = Bird(name="Player", color="red", x=50, y=256)

    bird.load_frames()
    if not bird.cframe:
        print("Erro: Frame do pássaro não carregado!")
        return

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(30)  # Limita a 30 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Atualizar lógica do jogo
        bird.move()
        background.move()
        floor.move()

        for pipe in pipes:
            pipe.move()

        # Colisões
        if bird.check_collision_with_floor(floor.y):
            print("Colisão com o chão!")
            running = False
        for pipe in pipes:
            if pipe.collide(bird):
                print("Colisão com o cano!")
                running = False

        # Atualização e limpeza de canos
        if pipes and pipes[0].x < -pipes[0].UPPER_PIPE.get_width():
            pipes.pop(0)
        if len(pipes) == 0 or pipes[-1].x < config.WINDOW_SIZE[0] - config.PIPE_DISTANCE:
            pipes.append(Pipe(x=config.WINDOW_SIZE[0]))

        # Renderização
        screen.fill((0, 0, 0))  # Fundo preto para teste
        background.draw(screen)
        floor.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        bird.draw(screen)
        pygame.display.update()

    pygame.quit()
