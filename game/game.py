import pygame
size = (30, 30)
draw_player = (930, 510)
px = 0
py = 0
clock = pygame.time.Clock()
def game(win, player_ct_im, player_t_im, test_map_back_im, test_map_walls_im, px, py, map_game, delta):
    keys = pygame.key.get_pressed()
    
    def draw_block(win, place, color):
            pygame.draw.rect(win, (color), ((px + place[0], py + place[1]), size))
            
    def check(px, py, place):
        if (draw_player[1] <= py + place[1] + size[1]) and (draw_player[1] + size[1] >= py + place[1]) and (draw_player[0] <= px + place[0] + size[0]) and (draw_player[0] + size[0] >= px + place[0]):
            return True
        else:
            return False
        
    def draw(win, player_ct_im, player_t_im, test_map_back_im, test_map_walls_im, px, py, map_game):
        if map_game == 'test':
            win.blit(test_map_back_im, (px, py))
            win.blit(test_map_walls_im, (px, py))
            win.blit(player_ct_im, draw_player)
            draw_block(win, (100, 100), (255, 255, 255))
            draw_block(win, (130, 130), (255, 255, 255))
            
    def move_player(win, keys, px, py, delta):
        if (keys[pygame.K_d]):
            if keys[pygame.K_s]:
                px = px + 106 * delta
                py = py + 106 * delta
            elif keys[pygame.K_w]:
                px = px + 106 * delta
                py = py - 106 * delta
            else:
                px = px + 150 * delta
                
        elif (keys[pygame.K_a]):
            if keys[pygame.K_s]:
                px = px - 106 * delta
                py = py + 106 * delta
            elif keys[pygame.K_w]:
                px = px - 106 * delta
                py = py - 106 * delta
            else:
                px = px - 150 * delta

        elif (keys[pygame.K_s]):
            py = py + 150 * delta
        elif (keys[pygame.K_w]):
            py = py - 150 * delta
            
        return (px, py)
 
    def log(win, keys, px, py, delta, map_game):
        (px_new, py_new) = move_player(win, keys, px, py, delta)
        if check(px_new, py_new, (100, 100)) == False and check(px_new, py_new, (130, 130)) == False:
            return(px_new, py_new)
        else:
            return(px, py)
        
    
    draw(win, player_ct_im, player_t_im, test_map_back_im, test_map_walls_im, px, py, map_game)
    (px, py) = log(win, keys, px, py, delta, map_game)
    return(px, py)
