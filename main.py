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
from load_images import *
from colors import *
from pygame.locals import * 

# ========================== Tratamento de dados Módulo ========================== #

try:
    pygame.init()
except:
    print('Erro inicialização de módulos.')

# ========================== Váriaveis usadas ========================== #
size = width, height = 1300, 760
screen = pygame.display.set_mode(size)
running = True
left, right, up, down = False, False, False, False
speed, p_x, p_y = 5, 0, 650
walkcont = 0
fps = 30
clock = pygame.time.Clock()

# ========================== Tamanho do bloco(tile) comparado ao tamanho da tela ========================== #
WIDTH, HEIGHT, TILE = 35, 19, 40


def redrawGameWindow():
    global walkcont, speed, p_x, p_y

    for y in range(HEIGHT):
        for x in range(WIDTH):
            screen.blit(tile[tilemap[y][x]], (x*TILE, y*TILE))
            
    for y in range(-6, HEIGHT):
        for x in range(-4, WIDTH):
            if objmap[y][x] < 24:
                screen.blit(obj[objmap[y][x]], (x*TILE, y*TILE))

    if walkcont + 1 >= 9:
        walkcont = 0

    if left:
        p_x -= speed
        screen.blit(walk_left[walkcont//3], [p_x, p_y])
        walkcont += 1
    
    elif right:
        p_x += speed
        screen.blit(walk_right[walkcont//3], [p_x, p_y])
        walkcont += 1
    
    elif up:
        p_y -= speed
        screen.blit(walk_up[walkcont//3], [p_x, p_y])
        walkcont += 1
    
    elif down:
        p_y += speed
        screen.blit(walk_front[walkcont//3], [p_x, p_y])
        walkcont += 1
    
    else:
        screen.blit(walk_front[1], [p_x, p_y])
       
    pygame.display.update()

        
# # ========================== Titulo e Icone ========================== #
pygame.display.set_caption('In The Moon')
pygame.display.set_icon(icon)

# ========================== Main ========================== #
while running: 
    clock.tick(fps)
    redrawGameWindow()

# ========================== QUIT e ESC para sair ========================== #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                       
            running = False

        if event.type == pygame.KEYDOWN:                    
            if event.key == pygame.K_ESCAPE: 
                running = False

# ========================== Interação com jogador, teclado movimentação ========================== #
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                left = True
                right = False
                up = False
                down = False

        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                right = True
                left = False
                up = False
                down = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                up = True
                right = False
                left = False
                down = False

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                down = True
                right = False
                left = False
                up = False

        else:
            left = False
            right = False
            up = False
            down = False
            walkcont = 0

# ==========================  ========================== #


