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
    Avalia cada genoma (um pássaro controlado por IA).
    Esta função é chamada pelo NEAT em cada geração.
    
    Args:
        genomes: Lista de genomas para serem avaliados.
        neat_config: Configurações do NEAT para a simulação.
    """
    birds = []  # Lista de pássaros controlados pela IA
    nets = []   # Redes neurais associadas a cada genoma
    ge = []     # Genomas correspondentes para avaliação

    # Inicializa o Pygame e configura a janela de exibição
    pygame.init()
    screen = pygame.display.set_mode(config.WINDOW_SIZE)
    pygame.display.set_caption("Flappy Bird - IA")  # Título da janela
    clock = pygame.time.Clock()  # Controle de tempo para o jogo

    # Inicializar objetos principais do jogo
    background = Background()
    background.load_sprite()

    floor = Floor(y=400)  # Define a posição do piso
    floor.load_sprite()

    pipes = [Pipe(x=config.WINDOW_SIZE[0])]  # Inicializa a lista de canos

    # Configura os pássaros para cada genoma
    for genome_id, genome in genomes:
        genome.fitness = 0  # Cada genoma começa com fitness 0
        net = neat.nn.FeedForwardNetwork.create(genome, neat_config)  # Cria a rede neural
        nets.append(net)

        bird = Bird(name=f"Bird-{genome_id}", color="yellow", x=50, y=256)  # Define o pássaro
        bird.load_frames()  # Carrega os sprites para o pássaro
        birds.append(bird)
        ge.append(genome)

    running = True  # Variável de controle para o loop principal do jogo

    while running and birds:  # O loop termina se não houver mais pássaros ou se o jogador sair
        # clock.tick(240)  # (Opcional) Controle de FPS, desativado para melhor fluidez

        # Captura eventos do Pygame (como fechar a janela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Evento de saída
                running = False

        # Atualiza os objetos do jogo
        background.move()  # Move o fundo para criar efeito de deslocamento
        floor.move()  # Move o piso

        # Itera sobre cada pássaro ainda "vivo"
        for i, bird in enumerate(birds):
            bird.move()  # Aplica gravidade e movimento no pássaro
            ge[i].fitness += 0.1  # Incrementa o fitness a cada frame sobrevivido

            # Entradas para a rede neural (posição do pássaro e distância para os canos)
            inputs = (
                bird.y,  # Posição vertical do pássaro
                abs(bird.y - pipes[0].height),  # Distância do pássaro ao topo do primeiro cano
                abs(bird.y - pipes[0].bottom),  # Distância do pássaro ao fundo do primeiro cano
            )
            output = nets[i].activate(inputs)  # Ativação da rede neural

            # Decisão da IA: se o output for maior que 0.5, o pássaro "salta"
            if output[0] > 0.5:
                bird.jump()

            # Verifica se o pássaro colidiu com o piso ou com um cano
            if bird.check_collision_with_floor(400) or pipes[0].collide(bird):
                ge[i].fitness -= 1  # Penaliza o fitness por colisão
                birds.pop(i)  # Remove o pássaro da lista
                nets.pop(i)   # Remove a rede neural associada
                ge.pop(i)     # Remove o genoma associado

        # Move os canos existentes
        for pipe in pipes:
            pipe.move()

        # Remove canos fora da tela e adiciona novos
        if pipes and pipes[0].x < -pipes[0].UPPER_PIPE.get_width():
            pipes.pop(0)  # Remove cano antigo
        if len(pipes) == 0 or pipes[-1].x < config.WINDOW_SIZE[0] - config.PIPE_DISTANCE:
            pipes.append(Pipe(x=config.WINDOW_SIZE[0]))  # Adiciona um novo cano

        # Renderiza os objetos do jogo
        screen.fill((135, 206, 250))  # Cor de fundo (azul claro)
        background.draw(screen)
        floor.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        for bird in birds:
            bird.draw(screen)

        pygame.display.update()  # Atualiza a tela com as renderizações

    pygame.quit()  # Fecha o Pygame ao fim do jogo

# Função principal para configurar e rodar o NEAT
def run_neat(config_path):
    """
    Configura e executa o algoritmo NEAT.
    
    Args:
        config_path: Caminho para o arquivo de configuração do NEAT.
    """
    neat_config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    # Inicializa a população com base nas configurações
    population = neat.Population(neat_config)

    # Adiciona relatórios no terminal e coleta estatísticas
    population.add_reporter(neat.StdOutReporter(True))  # Mostra as gerações no terminal
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    # Executa o NEAT por 50 gerações
    winner = population.run(eval_genomes, 50)
    print(f"Genoma vencedor: {winner}")

# Ponto de entrada para o script
if __name__ == "__main__":
    config_path = os.path.join(os.path.dirname(__file__), "config-feedforward.txt")
    run_neat(config_path)
