############################################################################
# Purpose : A very small, basic and my first game
# Usages : Learning purpose, Entertainment
# Start date : 17/05/2019
# End date :
# Author : Cleiton Pereira
# License : 
# Version : 1.0
############################################################################

import pygame
from colors import *

try:
    pygame.init()
except:
    print('Erro inicialização de módulos.')

size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
running = True

# Load Images
icon = pygame.image.load('_images/rocket.png')
bg_initial = pygame.image.load('_images/gameover.png')

walk_right = [pygame.image.load('_images/_player/player_d01.png'),
              pygame.image.load('_images/_player/player_d02.png'),
              pygame.image.load('_images/_player/player_d03.png')]

walk_left = [pygame.image.load('_images/_player/player_e01.png'),
              pygame.image.load('_images/_player/player_e02.png'),
              pygame.image.load('_images/_player/player_e03.png')]

walk_up = [pygame.image.load('_images/_player/player_c01.png'),
              pygame.image.load('_images/_player/player_c02.png'),
              pygame.image.load('_images/_player/player_c03.png')]

walk_front = [pygame.image.load('_images/_player/player_f01.png'),
              pygame.image.load('_images/_player/player_f02.png'),
              pygame.image.load('_images/_player/player_f03.png')]

# Title and Icon
pygame.display.set_caption('In The Moon')
pygame.display.set_icon(icon)

# Main
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                       # Ao clicar no botão X ele sai do jogo
            running = False
        if event.type == pygame.KEYDOWN:                    # Ao apertar a tecla ESC ele também irá sair
            if event.key == pygame.K_ESCAPE: 
                running = False

        screen.blit(walk_right[1], [0, 0])                      # Seta o background no inicio da tela e do Jogo
        pygame.display.update()