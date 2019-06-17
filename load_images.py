import pygame, sys
import _pickle as cPickle

tile, obj = [], []

icon = pygame.image.load('_images/rocket.png')
bg_initial = pygame.image.load('_images/b_bg.png')

# ========================== Importa os arquivos de dados ja prontos com os numeros de cada posição ========================== #
with open('_data/tilemap.txt', 'rb') as pickle_file:
    tilemap = cPickle.load(pickle_file)

with open('_data/objmap.txt', 'rb') as pickle_file:
    objmap = cPickle.load(pickle_file)

# ========================== Adiciona cada imagem em uma posição de vetor ========================== #
for i in range(24):
    tile += [pygame.image.load((f'_images/tile{i}.png'))]
    obj += [pygame.image.load((f'_images/obj{i}.png'))]

# ========================== Carrega as imagens do player - (Maneira alternativa) ========================== #
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

# ==========================  ========================== #