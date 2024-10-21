import pygame
import time
import random

# Inicializar o pygame
pygame.init()

# Definir as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)

# Definir o tamanho da janela
largura = 600
altura = 400
tamanho_bloco = 10
velocidade = 15

# Criar a janela do jogo
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobra")

# Definir o relógio para controlar a velocidade do jogo
clock = pygame.time.Clock()

# Função para desenhar a cobra
def desenhar_cobra(tamanho_bloco, lista_cobra):
    for bloco in lista_cobra:
        pygame.draw.rect(janela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

# Função principal do jogo
def jogo():
    fim_jogo = False
    game_over = False

    # Posição inicial da cobra
    x_cobra = largura / 2
    y_cobra = altura / 2
    x_cobra_mudanca = 0
    y_cobra_mudanca = 0

    # Lista e comprimento inicial da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    x_comida = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    y_comida = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not fim_jogo:

        while game_over:
            janela.fill(preto)
            fonte = pygame.font.SysFont("arial", 35)
            mensagem = fonte.render("Você perdeu! Pressione C para jogar novamente ou Q para sair", True, vermelho)
            janela.blit(mensagem, [largura / 6, altura / 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_jogo = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cobra_mudanca = -tamanho_bloco
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cobra_mudanca = tamanho_bloco
                    y_cobra_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_cobra_mudanca = -tamanho_bloco
                    x_cobra_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_cobra_mudanca = tamanho_bloco
                    x_cobra_mudanca = 0

        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            game_over = True

        x_cobra += x_cobra_mudanca
        y_cobra += y_cobra_mudanca
        janela.fill(preto)

        pygame.draw.rect(janela, vermelho, [x_comida, y_comida, tamanho_bloco, tamanho_bloco])

        # Atualizar a posição da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for bloco in lista_cobra[:-1]:
            if bloco == cabeca_cobra:
                game_over = True

        desenhar_cobra(tamanho_bloco, lista_cobra)

        pygame.display.update()

        # Verificar se a cobra comeu a comida
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            y_comida = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo()
