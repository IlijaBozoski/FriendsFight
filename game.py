import pygame
import random
import sys

import colors

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1080, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FriendsFight")
input_font = pygame.font.SysFont("monospace", 30)


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
player1_name = ""
player2_name = ""

# Add a game state to control the flow
# game_state = "menu"  # Initial state is the menu
game_state = "daSeOdkomentiraMenu"
# Text input settings
active_input = None  # Tracks which input is active
input_box1 = pygame.Rect(WIDTH // 2 - 115, HEIGHT // 2 - 70, 300, 40)  # Player 1 input box
input_box2 = pygame.Rect(WIDTH // 2 - 115, HEIGHT // 2, 300, 40)       # Player 2 input box
start_button = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 2 + 70, 200, 50)  # Moved 20 pixels to the right


input_color_inactive = colors.WHITE
input_color_active = colors.LIGHTYELLOW
button_color = colors.YELLOW
# Game settings
clock = pygame.time.Clock()
score_player1 = 0
score_player2 = 0
font = pygame.font.SysFont("monospace", 35)
fontStartGame = pygame.font.SysFont("monospace", 25)

# Classes and Functions

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = bullet_size
        self.height = bullet_size
        self.direction = direction  # Direction is either 'up' or 'down'

    def move(self):
        if self.direction == 'up':
            self.y -= bullet_speed  # Move bullet upwards
        elif self.direction == 'down':
            self.y += bullet_speed  # Move bullet downwards

    def draw(self):
        pygame.draw.rect(screen, colors.WHITE, (self.x, self.y, self.width, self.height))

def create_asteroid():
    x_pos = random.randint(0, WIDTH - asteroid_size)
    y_pos = -asteroid_size
    return [x_pos, y_pos]

def draw_asteroids(asteroid_list):
    for asteroid_pos in asteroid_list:
        pygame.draw.rect(screen, colors.RED, (asteroid_pos[0], asteroid_pos[1], asteroid_size, asteroid_size))

def update_asteroid_positions(asteroid_list):
    global score_player1, score_player2
    for idx, asteroid_pos in enumerate(asteroid_list):
        if asteroid_pos[1] >= 0 and asteroid_pos[1] < HEIGHT:
            asteroid_pos[1] += asteroid_speed
        else:
            asteroid_list.pop(idx)
            score_player1 += 1
            score_player2 += 1

def collision_check(player_pos, asteroid_list):
    for asteroid_pos in asteroid_list:
        if (asteroid_pos[0] < player_pos[0] < asteroid_pos[0] + asteroid_size or
            asteroid_pos[0] < player_pos[0] + player_size < asteroid_pos[0] + asteroid_size):
            if (asteroid_pos[1] < player_pos[1] < asteroid_pos[1] + asteroid_size or
                asteroid_pos[1] < player_pos[1] + player_size < asteroid_pos[1] + asteroid_size):
                return True
    return False

def bullet_asteroid_collision(bullets, asteroid_list):
    global score_player1, score_player2
    for bullet in bullets:
        for idx, asteroid_pos in enumerate(asteroid_list):
            if (asteroid_pos[0] < bullet.x < asteroid_pos[0] + asteroid_size or
                asteroid_pos[0] < bullet.x + bullet_size < asteroid_pos[0] + asteroid_size):
                if (asteroid_pos[1] < bullet.y < asteroid_pos[1] + asteroid_size or
                    asteroid_pos[1] < bullet.y + bullet_size < asteroid_pos[1] + asteroid_size):
                    asteroid_list.pop(idx)  # Remove asteroid
                    bullets.remove(bullet)  # Remove bullet
                    score_player1 += 5  # Increase score for destroying an asteroid
                    score_player2 += 5

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))


while game_state == "menu":
    screen.fill(colors.PURPLE)

    # Event handling for the input screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if clicking in an input box
            if input_box1.collidepoint(event.pos):
                active_input = "player1"
            elif input_box2.collidepoint(event.pos):
                active_input = "player2"
            elif start_button.collidepoint(event.pos) and player1_name and player2_name:
                game_state = "game"  # Proceed to the game
            else:
                active_input = None
        elif event.type == pygame.KEYDOWN and active_input:
            if event.key == pygame.K_BACKSPACE:
                if active_input == "player1":
                    player1_name = player1_name[:-1]
                elif active_input == "player2":
                    player2_name = player2_name[:-1]
            else:
                if active_input == "player1":
                    player1_name += event.unicode
                elif active_input == "player2":
                    player2_name += event.unicode

    # Draw input boxes
    pygame.draw.rect(screen, input_color_active if active_input == "player1" else input_color_inactive, input_box1)
    pygame.draw.rect(screen, input_color_active if active_input == "player2" else input_color_inactive, input_box2)
    pygame.draw.rect(screen, button_color, start_button)

    # Render input text
    text_surface1 = input_font.render(player1_name, True, colors.BLACK)
    text_surface2 = input_font.render(player2_name, True, colors.BLACK)
    button_text = fontStartGame.render("Start Game", True, colors.RED)
    screen.blit(text_surface1, (input_box1.x + 10, input_box1.y + 5))
    screen.blit(text_surface2, (input_box2.x + 10, input_box2.y + 5))
    screen.blit(button_text, (start_button.x + 30, start_button.y + 10))

    # Render labels
    draw_text("Player 1:", font, colors.WHITE, screen, WIDTH // 2 - 300, HEIGHT // 2 - 70)
    draw_text("Player 2:", font, colors.WHITE, screen, WIDTH // 2 - 300, HEIGHT // 2)

    pygame.display.flip()
    clock.tick(30)

# Main game loop
game_over = False
while not game_over:
    screen.fill(colors.DARKBLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player 1 (Arrow Keys) movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1_pos[0] > 0:
        player1_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player1_pos[0] < WIDTH - player_size:
        player1_pos[0] += player_speed
    if keys[pygame.K_UP] and player1_pos[1] > HEIGHT * 2 / 3:  # Restrict upward movement
        player1_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player1_pos[1] < HEIGHT - player_size:
        player1_pos[1] += player_speed

    # Player 2 (WASD) movement (restricted to the top third)
    if keys[pygame.K_a] and player2_pos[0] > 0:
        player2_pos[0] -= player_speed
    if keys[pygame.K_d] and player2_pos[0] < WIDTH - player_size:
        player2_pos[0] += player_speed
    if keys[pygame.K_w] and player2_pos[1] > 0:
        player2_pos[1] -= player_speed
    if keys[pygame.K_s] and player2_pos[1] < HEIGHT / 3 - player_size:  # Restrict downward movement
        player2_pos[1] += player_speed

    # Shooting bullets for player 1
    if keys[pygame.K_SPACE]:
        new_bullet1 = Bullet(player1_pos[0] + player_size // 2 - bullet_size // 2, player1_pos[1], 'up')
        player1_bullets.append(new_bullet1)

    # Shooting bullets for player 2
    if keys[pygame.K_RETURN]:  # Use Enter key for player 2 shooting
        new_bullet2 = Bullet(player2_pos[0] + player_size // 2 - bullet_size // 2, player2_pos[1], 'down')
        player2_bullets.append(new_bullet2)

    # Update and draw asteroids
    if random.randint(1, 20) == 1:  # Random chance to spawn an asteroid
        asteroid_list.append(create_asteroid())

    update_asteroid_positions(asteroid_list)
    draw_asteroids(asteroid_list)

    # Move and draw player 1's bullets
    for bullet in player1_bullets[:]:
        bullet.move()
        bullet.draw()

    # Move and draw player 2's bullets
    for bullet in player2_bullets[:]:
        bullet.move()
        bullet.draw()

    # Check collisions between bullets and asteroids
    bullet_asteroid_collision(player1_bullets, asteroid_list)
    bullet_asteroid_collision(player2_bullets, asteroid_list)

    # Collision detection between players and asteroids
    if collision_check(player1_pos, asteroid_list) or collision_check(player2_pos, asteroid_list):
        game_over = True
        break

    # Draw players
    pygame.draw.rect(screen, colors.GREEN, (player1_pos[0], player1_pos[1], player_size, player_size))  # Player 1
    pygame.draw.rect(screen, colors.WHITE, (player2_pos[0], player2_pos[1], player_size, player_size))  # Player 2

    # Draw scores
    draw_text(f"{player1_name}: {score_player1}", font, colors.WHITE, screen, 10, 10)
    draw_text(f"{player2_name}: {score_player2}", font, colors.WHITE, screen, WIDTH - 200, 10)

    pygame.display.flip()
    clock.tick(30)

# Game over screen
screen.fill(colors.DARKBLUE)
draw_text("Game Over", font, colors.WHITE, screen, WIDTH // 2 - 100, HEIGHT // 2)
draw_text(f"Player 1 Final Score: {score_player1}", font, colors.WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2 + 40)
draw_text(f"Player 2 Final Score: {score_player2}", font, colors.WHITE, screen, WIDTH // 2 - 150, HEIGHT // 2 + 80)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
sys.exit()
