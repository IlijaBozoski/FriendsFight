
import pygame
import colors
import settings



class Rocket:
    def __init__(self, x, y, direction,delta_time):
        self.delta_time = delta_time
        self.x = x
        self.y = y
        self.width = 40
        self.height = 80
        self.image = pygame.image.load('images/r-removebg-preview.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.direction = direction

    def move(self):
        if self.direction == 'up':
            self.y -=70+self.delta_time  # Move bullet upwards
        elif self.direction == 'down':
            self.y += 70+self.delta_time  # Move bullet downwards

    def draw(self):
        settings.screen.blit(self.image, (self.x, self.y))

class RocketRevered:
    def __init__(self, x, y, direction,delta_time):
        self.delta_time = delta_time
        self.x = x
        self.y = y
        self.width = 40
        self.height = 80
        self.image = pygame.image.load('images/r-removebg-preview-reversed.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.direction = direction
    def move(self):
        if self.direction == 'up':
            self.y -=70+self.delta_time  # Move bullet upwards
        elif self.direction == 'down':
            self.y += 70+self.delta_time  # Move bullet downwards

    def draw(self):
        settings.screen.blit(self.image, (self.x, self.y))