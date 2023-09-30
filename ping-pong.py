import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações do jogo
largura = 800
altura = 600
tamanho_raquete = 100
tamanho_bola = 20
velocidade_raquete = 10
velocidade_bola = 5
cor_branca = (255, 255, 255)

# Configuração da tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

# Posições iniciais das raquetes e da bola
raquete_esquerda = pygame.Rect(50, altura // 2 - tamanho_raquete // 2, 20, tamanho_raquete)
raquete_direita = pygame.Rect(largura - 50 - 20, altura // 2 - tamanho_raquete // 2, 20, tamanho_raquete)
bola = pygame.Rect(largura // 2 - tamanho_bola // 2, altura // 2 - tamanho_bola // 2, tamanho_bola, tamanho_bola)

# Velocidades iniciais da bola
velocidade_x = velocidade_bola
velocidade_y = velocidade_bola

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação das raquetes
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and raquete_esquerda.top > 0:
        raquete_esquerda.y -= velocidade_raquete
    if teclas[pygame.K_s] and raquete_esquerda.bottom < altura:
        raquete_esquerda.y += velocidade_raquete
    if teclas[pygame.K_UP] and raquete_direita.top > 0:
        raquete_direita.y -= velocidade_raquete
    if teclas[pygame.K_DOWN] and raquete_direita.bottom < altura:
        raquete_direita.y += velocidade_raquete

    # Movimentação da bola
    bola.x += velocidade_x
    bola.y += velocidade_y

    # Verifica colisões com as bordas
    if bola.top <= 0 or bola.bottom >= altura:
        velocidade_y = -velocidade_y

    # Verifica colisões com as raquetes
    if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
        velocidade_x = -velocidade_x

    # Verifica se a bola saiu da tela (ponto marcado)
    if bola.left <= 0 or bola.right >= largura:
        # Reinicia a posição da bola
        bola.x = largura // 2 - tamanho_bola // 2
        bola.y = altura // 2 - tamanho_bola // 2
        velocidade_x = -velocidade_x

    # Preenche a tela com a cor de fundo
    tela.fill((0, 0, 0))

    # Desenha as raquetes e a bola
    pygame.draw.rect(tela, cor_branca, raquete_esquerda)
    pygame.draw.rect(tela, cor_branca, raquete_direita)
    pygame.draw.ellipse(tela, cor_branca, bola)

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de quadros por segundo
    pygame.time.Clock().tick(60)
