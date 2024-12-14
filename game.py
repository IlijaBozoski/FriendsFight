import pygame
import random
import sys

import scoreManipulations
import settings
from Bullet import Bullet
import colors

# Initialize Pygame
pygame.init()
player1_name = ""
player2_name = ""

# Add a game state to control the flow
game_state = "menu"  # Initial state is the menu
# game_state = "menu1"  # Initial state is the menu

# Text input settings
active_input = None  # Tracks which input is active
input_box1 = pygame.Rect(settings.WIDTH // 2 - 115, settings.HEIGHT // 2 - 70, 300, 40)  # Player 1 input box
input_box2 = pygame.Rect(settings.WIDTH // 2 - 115, settings.HEIGHT  // 2, 300, 40)       # Player 2 input box
start_button = pygame.Rect(settings.WIDTH // 2 - 60, settings.HEIGHT  // 2 + 70, 200, 50)  # Moved 20 pixels to the right

input_font = pygame.font.SysFont("monospace", 30)
planes=[['images/cessna-removebg-preview.png',"images/cessna-removebg-reversed-preview.png"],
        ["images/mustang-removebg-preview.png","images/mustang-removebg-reversed-preview.png"],
        ["images/avionce.png","images/avioncePrevrteno.png"],
        ["images/mig-removebg-preview.png","images/mig-removebg-reversed-preview.png"],
        ["images/f16-removebg-preview.png","images/f16-removebg-reversed-preview.png"],
        ["images/b2-removebg-preview.png","images/b2-removebg-reverse-preview.png"]]
# Game settings
clock = pygame.time.Clock()
score_player1 = 0
score_player2 = 0
font = pygame.font.SysFont("monospace", 35)
fontStartGame = pygame.font.SysFont("monospace", 25)
def handle_player(player_name):
    user=scoreManipulations.userExists(player_name)
    if user:
        score=user[1]
        level=scoreManipulations.findBulletLevels(int (score))
        plane=scoreManipulations.findPlane(int(score))
        level.append(plane)
        return level
    else:
        level=[0,0,0]
        return level



def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    surface.blit(text_obj, (x, y))
def check_collision():
    global score_player1, score_player2

    # Check if any player 1's bullets collide with player 2
    for bullet in settings.player1_bullets[:]:
        if (settings.player2_pos[0] < bullet.x < settings.player2_pos[0] + settings.player_size and
            settings.player2_pos[1] < bullet.y < settings.player2_pos[1] + settings.player_size):
            score_player1 += 5  # Player 1 gets 10 points
            settings.player1_bullets.remove(bullet)  # Remove the bullet after it hits

    # Check if any player 2's bullets collide with player 1
    for bullet in settings.player2_bullets[:]:
        if (settings.player1_pos[0] < bullet.x < settings.player1_pos[0] + settings.player_size and
            settings.player1_pos[1] < bullet.y < settings.player1_pos[1] + settings.player_size):
            score_player2 += 5  # Player 2 gets 10 points
            settings.player2_bullets.remove(bullet)  # Remove the bullet after it hits

def check_game_over(player1_score, player2_score, screen, font):

    if player1_score >= 300 or player2_score >= 300:
        scoreManipulations.updateScores(player1_name,player1_score,player2_name,player2_score)
        screen.fill((0, 0, 0))  # Clear the screen
        winner = player1_name if player1_score >= 300 else player2_name
        game_over_text = font.render(f"Game Over! {winner} Wins!", True, (255, 255, 255))
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2,
                                     screen.get_height() // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait for 3 seconds before exiting
        return True
    return False

while game_state == "menu":
    settings.screen.fill(colors.PURPLE)

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
    pygame.draw.rect(settings.screen, settings.input_color_active if active_input == "player1" else settings.input_color_inactive, input_box1)
    pygame.draw.rect(settings.screen, settings.input_color_active if active_input == "player2" else settings.input_color_inactive, input_box2)
    pygame.draw.rect(settings.screen, settings.button_color, start_button)

    # Render input text
    text_surface1 = input_font.render(player1_name, True, colors.BLACK)
    text_surface2 = input_font.render(player2_name, True, colors.BLACK)
    button_text = fontStartGame.render("Start Game", True, colors.RED)
    settings.screen.blit(text_surface1, (input_box1.x + 10, input_box1.y + 5))
    settings.screen.blit(text_surface2, (input_box2.x + 10, input_box2.y + 5))
    settings.screen.blit(button_text, (start_button.x + 30, start_button.y + 10))

    # Render labels
    draw_text("Player 1:", font, colors.WHITE, settings.screen, settings.WIDTH // 2 - 300, settings.HEIGHT // 2 - 70)
    draw_text("Player 2:", font, colors.WHITE, settings.screen, settings.WIDTH // 2 - 300, settings.HEIGHT // 2)

    pygame.display.flip()
    clock.tick(30)

# Main game loop
game_over = False
while not game_over:
    settings.screen.fill(colors.DARKBLUE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player 1 (Arrow Keys) movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and settings.player1_pos[0] > 0:
        settings.player1_pos[0] -= settings.player_speed
    if keys[pygame.K_RIGHT] and settings.player1_pos[0] < settings.WIDTH - settings.player_size:
        settings.player1_pos[0] += settings.player_speed
    if keys[pygame.K_UP] and settings.player1_pos[1] > settings.HEIGHT * 2 / 3:
        settings.player1_pos[1] -= settings.player_speed
    if keys[pygame.K_DOWN] and settings.player1_pos[1] < settings.HEIGHT - settings.player_size:
        settings.player1_pos[1] += settings.player_speed

    # Player 2 (WASD) movement
    if keys[pygame.K_a] and settings.player2_pos[0] > 0:
        settings.player2_pos[0] -= settings.player_speed
    if keys[pygame.K_d] and settings.player2_pos[0] < settings.WIDTH - settings.player_size:
        settings.player2_pos[0] += settings.player_speed
    if keys[pygame.K_s] and settings.player2_pos[1] > 0:
        settings.player2_pos[1] -= settings.player_speed
    if keys[pygame.K_w] and settings.player2_pos[1] < settings.HEIGHT / 3 - settings.player_size:
        settings.player2_pos[1] += settings.player_speed

    # Shooting bullets for player 1
    if keys[pygame.K_RETURN]:
        level = handle_player(player1_name)
        settings.setBulletParams(level[0], level[1])
        new_bullet1 = Bullet(settings.player1_pos[0] + settings.player_size // 2 - settings.bullet_size // 2, settings.player1_pos[1], 'up')
        settings.player1_bullets.append(new_bullet1)

    # Shooting bullets for player 2
    if keys[pygame.K_SPACE]:
        level = handle_player(player2_name)
        settings.setBulletParams(level[0], level[1])
        new_bullet2 = Bullet(settings.player2_pos[0] + settings.player_size // 2 - settings.bullet_size // 2, settings.player2_pos[1], 'down')
        settings.player2_bullets.append(new_bullet2)

    # Move and draw bullets
    for bullet in settings.player1_bullets[:]:
        bullet.move()
        bullet.draw()

    for bullet in settings.player2_bullets[:]:
        bullet.move()
        bullet.draw()

    # Check for collisions and update score
    check_collision()

    # Draw players
    plane1=handle_player(player1_name)[2]
    plane2=handle_player(player2_name)[2]
    player1_image = pygame.image.load(planes[plane1][0])
    player2_image = pygame.image.load(planes[plane2][1])
    scaled_width = settings.player_size * 1.5
    scaled_height = settings.player_size * 1.5
    player1_image = pygame.transform.scale(player1_image, (scaled_width, scaled_height))
    player2_image = pygame.transform.scale(player2_image, (scaled_width, scaled_height))
    settings.screen.blit(player1_image, (settings.player1_pos[0], settings.player1_pos[1]))
    settings.screen.blit(player2_image, (settings.player2_pos[0], settings.player2_pos[1]))

    # Draw scores
    draw_text(f"{player1_name}: {score_player1}", font, colors.WHITE, settings.screen, 10, 10)
    draw_text(f"{player2_name}: {score_player2}", font, colors.WHITE, settings.screen, settings.WIDTH - 200, 10)

    # Check for game over
    if check_game_over(score_player1, score_player2, settings.screen, font):
        game_over = True

    pygame.display.flip()
    clock.tick(30)

# Cleanup
pygame.quit()
sys.exit()