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

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
running = True

# Load Images
icon = pygame.image.load('_images/rocket.png')

# Title and Icon
pygame.display.set_caption('Space Robot')
pygame.display.set_icon(icon)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(random_colors[1])      
        pygame.display.update()