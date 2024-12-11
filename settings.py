import pygame

import colors

# Screen dimensions
WIDTH, HEIGHT = 1080, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FriendsFight")


# Player settings
bullet_list_size=[1,2,3,4,5,6,7,8,9,10]
bullet_list_speed=[6,7,8,9,10,11,12,13,14,15]
player_size = 50
player_speed = 10
bullet_size = bullet_list_size[1]
bullet_speed = bullet_list_speed[9]

# Player positions
player1_pos = [WIDTH // 2, HEIGHT - 2 * player_size]  # Player 1 at the bottom
player2_pos = [WIDTH // 2, 50]  # Player 2 at the top

# Bullet lists
player1_bullets = []
player2_bullets = []

# Asteroid settings
asteroid_size = 50
asteroid_speed = 5
asteroid_list = []


input_color_inactive = colors.WHITE
input_color_active = colors.LIGHTYELLOW
button_color = colors.YELLOW