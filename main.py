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


from pygame.event import Event

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
speed, p_x, p_y = 2, width/2, height /2
walkcont = 0
fps = 30
clock = pygame.time.Clock()


slide_x = 0
slide_y = 0
moving = (0, 0)

# ========================== Tamanho do bloco(tile) comparado ao tamanho da tela ========================== #
WIDTH, HEIGHT, TILE = 35, 19, 40
MIDDLE = WIDTH/2 - 1 , HEIGHT/2 - 1
GOTO = 24 # levar o seu personagem para posicao do evento
SETOBJECT = 26 # colocar um objeto no mapa

# ========================== Funções usadas ========================== #
def handle():
    global running, moving
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                       
            running = False

        if event.type == pygame.KEYDOWN:                    
            if event.key == pygame.K_ESCAPE: 
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key in MOVES.keys():
                moving = (moving[0] + MOVES[event.key][0],
                          moving[1] + MOVES[event.key][1])

        if event.type == pygame.KEYUP:
            if event.key in MOVES.keys():
                moving = (moving[0] - MOVES[event.key][0],
                          moving[1] - MOVES[event.key][1])
                
        if event.type == GOTO:
            goto(event.x, event.y)

        elif event.type == SETOBJECT:
            objmap[event.x][event.y] = event.obj

def goto(x, y):
	global slide_x, slide_y
	slide_x = x - MIDDLE[0]
	slide_y = y - MIDDLE[1]
	pygame.display.set_caption(f"MMORPG Client - Pos: {int(x)}, {int(y)}")

def move(inc_x, inc_y):
	if inc_x != 0 or inc_y != 0:
		e = Event(GOTO, {'x': slide_x + inc_x + MIDDLE[0], 'y': slide_y + inc_y + MIDDLE[1]})
		pygame.event.post(e)

MOVES = {
    K_RIGHT: (1, 0),
    K_LEFT : (-1, 0),
    K_UP   : (0, -1),
    K_DOWN : (0, 1)
}


def animation():
    global walkcont, p_x, p_y
    
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
        
# # ========================== Icone ========================== #
pygame.display.set_icon(icon)

# ========================== Main ========================== #
while running: 
    clock.tick(fps)
    handle()
    move(moving[0], moving[1])
    pygame.display.update()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            i, j = (int(slide_x) + x, int(slide_y) + y)
            screen.blit(tile[tilemap[j][i]], (x*TILE, y*TILE))
    for y in range(-6, HEIGHT):
        for x in range(-4, WIDTH):
            i, j = (x + int(slide_x), int(slide_y) + y)
            if objmap[j][i] < 24:
                screen.blit(obj[objmap[j][i]], (x*TILE, y*TILE))
# ==========================  ========================== #