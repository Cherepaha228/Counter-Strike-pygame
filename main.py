import pygame
import random
from game.pre_game import *
from game.game import *
pygame.init()
win = pygame.display.set_mode((1920, 1080))#, pygame.FULLSCREEN
map_game = 'test'

(player_ct_im, player_t_im, test_map_back_im, test_map_walls_im) = pre_game()

clock = pygame.time.Clock()
while True:
    pygame.draw.rect(win, (0,0,0),  (-10000,-10000, 20000,20000))
    clock.tick(60)
    delta = clock.get_time() / 1000
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    if (keys[pygame.K_ESCAPE]):
        exit()
    (px, py) = game(win, player_ct_im, player_t_im, test_map_back_im, test_map_walls_im, px, py, map_game, delta)
    pygame.display.update()

