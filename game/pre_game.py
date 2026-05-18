import pygame
def pre_game():
    def file_load():
        player_ct_im = pygame.image.load('resources\\models\\ct.png')
        player_t_im = pygame.image.load('resources\\models\\t.png')
        test_map_back_im = pygame.image.load('resources\\maps\\test_map\\background.png')
        test_map_walls_im = pygame.image.load('resources\\maps\\test_map\\walls.png')
        return(player_ct_im, player_t_im, test_map_back_im, test_map_walls_im)
    (player_ct_im, player_t_im, test_map_back_im, test_map_walls_im) = file_load()
    return(player_ct_im, player_t_im, test_map_back_im, test_map_walls_im)
