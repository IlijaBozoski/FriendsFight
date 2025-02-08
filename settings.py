import pygame

import colors

# Screen dimensions
WIDTH, HEIGHT = 1080, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FriendsFight")

bullet_list_size=[1,2,3,4,5,6,7,8,9,10]
bullet_list_speed=[6,7,8,9,10,11,12,13,14,15]
player_size = 50
player_speed = 10
bullet_size = bullet_list_size[0]
bullet_speed = bullet_list_speed[0]
player1_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player2_pos = [WIDTH // 2, 50]
player1_bullets = []
player2_bullets = []
asteroid_size = 50
asteroid_speed = 5
asteroid_list = []
input_color_inactive = colors.WHITE
input_color_active = colors.LIGHTYELLOW
button_color = colors.YELLOW
def setBulletParams(lvl1,lvl2):
    global bullet_size, bullet_speed
    bullet_size = bullet_list_size[lvl1]
    bullet_speed = bullet_list_speed[lvl2]