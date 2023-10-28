import pygame
from sys import exit
from random import choice, randint

def aleatorio():
    randint(-5,5)

def mostra_textos():
    global p1, p2
    player1 = fonte_pixel.render(str(p1), True, (255, 255, 255))
    p1_rect = player1.get_rect(center=(11, 20))
    player2 = fonte_pixel.render(str(p2), True, (255, 255, 255))
    p2_rect = player2.get_rect(center=(790, 20))

    tela.blit(player1, p1_rect)
    tela.blit(player2, p2_rect)

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura = 800
altura = 600
tamanho_bola = 20
velocidade_raquete = 10
velocidade_bola = 10

# Configuração da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("PyPong")

# Carrega o plano de fundo
plano_fundo = []
for imagem in range(1, 9):
    img = pygame.image.load(f'imagens/inteiro/origbig{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (800, 600))
    plano_fundo.append(img)

# Seleciona um fundo aleatorio 
papel_parede_aleatorio = choice(plano_fundo)

# Imagem da raquete
raquete = []
for imagem in range(1, 6):
    img = pygame.image.load(f'barras/{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (40, 110))
    raquete.append(img)

# Seleciona uma raquete aleatoria
raquete_esquerda = choice(raquete)
raquete_direita = choice(raquete)

raquete_esquerda_rect = raquete_esquerda.get_rect(center=(70, 280))
raquete_direita_rect = raquete_direita.get_rect(center=(720, 280))

bola = pygame.Rect(largura // 2 - tamanho_bola // 2, altura // 2 - tamanho_bola // 2, tamanho_bola, tamanho_bola)

# Carrega os arquivos necessários para o jogo
fonte_pixel = pygame.font.Font('font/Pixeltype.ttf', 50)

# Velocidades iniciais da bola
velocidade_x = velocidade_bola
velocidade_y = 0

#informaçao do placar
p1 = 0
p2 = 0

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Movimentação das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete_esquerda_rect.top > 0:
        raquete_esquerda_rect.y -= velocidade_raquete
    if teclas[pygame.K_s] and raquete_esquerda_rect.bottom < altura:
        raquete_esquerda_rect.y += velocidade_raquete
    if teclas[pygame.K_UP] and raquete_direita_rect.top > 0:
        raquete_direita_rect.y -= velocidade_raquete
    if teclas[pygame.K_DOWN] and raquete_direita_rect.bottom < altura:
        raquete_direita_rect.y += velocidade_raquete
    if teclas[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    # Movimentação da bola
    bola.x += velocidade_x
    bola.y += velocidade_y

    # Verifica colisões com as bordas
    if bola.top <= 0 or bola.bottom >= altura:
        velocidade_y = -velocidade_y

    # Verifica colisões com as raquetes
    if bola.left <= 70:
        p2 += 1
        bola.x = largura // 2 - tamanho_bola // 2
        bola.y = altura // 2 - tamanho_bola // 2
        velocidade_x = -velocidade_x
    if bola.right >= 730:
        p1 += 1
        bola.x = largura // 2 - tamanho_bola // 2
        bola.y = altura // 2 - tamanho_bola // 2
        velocidade_x = -velocidade_x

    if bola.colliderect(raquete_direita_rect) or bola.colliderect(raquete_esquerda_rect):
        velocidade_x = -velocidade_x
        velocidade_y = randint(-6,6)

    if p1 == 3:
        print("================================================================")
        print("================= Jogador 1 é o Vendedor!!! ====================")
        print("================================================================")
        pygame.quit()
        exit()
    elif p2 == 3:
        print("================================================================")
        print("================= Jogador 2 é o Vendedor!!! ====================")
        print("================================================================")
        pygame.quit()
        exit()
        
    # Desenha o plano de fundo
    tela.blit(papel_parede_aleatorio, (0, 0))

    # Desenha as raquetes e a bola
    tela.blit(raquete_esquerda, raquete_esquerda_rect)
    tela.blit(raquete_direita, raquete_direita_rect)
    pygame.draw.ellipse(tela, 'gray', bola)

    # Placar
    mostra_textos()

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de quadros por segundo
    pygame.time.Clock().tick(60)
