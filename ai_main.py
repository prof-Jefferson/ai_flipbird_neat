import pygame
import neat
import os
from GameObjects.Background import Background
from GameObjects.Floor import Floor
from GameObjects.Bird import Bird
from GameObjects.Pipe import Pipe
import config

# Função de avaliação para o NEAT
def eval_genomes(genomes, neat_config):
    """
    Avalia os genomas, cada um controlando um pássaro.
    """
    birds = []
    nets = []
    ge = []

    # Inicializar o Pygame antes de carregar qualquer sprite
    pygame.init()
    screen = pygame.display.set_mode(config.WINDOW_SIZE)
    pygame.display.set_caption("Flappy Bird - IA")
    clock = pygame.time.Clock()

    # Inicializar objetos do jogo
    background = Background()
    background.load_sprite()

    floor = Floor(y=400)
    floor.load_sprite()

    pipes = [Pipe(x=config.WINDOW_SIZE[0])]

    # Criar os pássaros e carregar os frames após pygame.init()
    for genome_id, genome in genomes:
        genome.fitness = 0  # Fitness inicial
        net = neat.nn.FeedForwardNetwork.create(genome, neat_config)
        nets.append(net)

        bird = Bird(name=f"Bird-{genome_id}", color="yellow", x=50, y=256)
        bird.load_frames()  # Garantir que pygame.display está inicializado antes de chamar
        birds.append(bird)
        ge.append(genome)

    running = True
    while running and birds:
        #clock.tick(240)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        background.move()
        floor.move()

        for i, bird in enumerate(birds):
            bird.move()
            ge[i].fitness += 0.1  # Incremento de fitness por sobrevivência

            inputs = (
                bird.y,
                abs(bird.y - pipes[0].height),
                abs(bird.y - pipes[0].bottom),
            )
            output = nets[i].activate(inputs)

            if output[0] > 0.5:
                bird.jump()

            if bird.check_collision_with_floor(400) or pipes[0].collide(bird):
                ge[i].fitness -= 1
                birds.pop(i)
                nets.pop(i)
                ge.pop(i)

        for pipe in pipes:
            pipe.move()

        if pipes and pipes[0].x < -pipes[0].UPPER_PIPE.get_width():
            pipes.pop(0)
        if len(pipes) == 0 or pipes[-1].x < config.WINDOW_SIZE[0] - config.PIPE_DISTANCE:
            pipes.append(Pipe(x=config.WINDOW_SIZE[0]))

        screen.fill((135, 206, 250))
        background.draw(screen)
        floor.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        for bird in birds:
            bird.draw(screen)

        pygame.display.update()

    pygame.quit()

# Função principal para configurar e rodar o NEAT
def run_neat(config_path):
    """
    Configura o NEAT e executa o treinamento.
    """
    neat_config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    # Configura e inicializa a população
    population = neat.Population(neat_config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    # Executa o NEAT
    winner = population.run(eval_genomes, 50)
    print(f"Genoma vencedor: {winner}")

# Ponto de entrada para o script
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "config-feedforward.txt")
    run_neat(config_path)
