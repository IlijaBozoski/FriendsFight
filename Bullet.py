
import pygame
import colors
import settings


class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = settings.bullet_size
        self.height = settings.bullet_size
        self.direction = direction  # Direction is either 'up' or 'down'

    def move(self):
        if self.direction == 'up':
            self.y -=settings.bullet_speed  # Move bullet upwards
        elif self.direction == 'down':
            self.y += settings.bullet_speed  # Move bullet downwards

    def draw(self):
        pygame.draw.rect(settings.screen, colors.WHITE, (self.x, self.y, self.width, self.height))