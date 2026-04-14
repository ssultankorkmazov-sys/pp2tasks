import pygame

class Ball:
    def __init__(self, x, y, radius=25, speed=10):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = (255, 0, 0)

    def move(self, dx, dy, screen_width, screen_height):
        new_x = self.x + dx
        new_y = self.y + dy

        # borders
        if new_x - self.radius >= 0 and new_x + self.radius <= screen_width:
            self.x = new_x

        if new_y - self.radius >= 0 and new_y + self.radius <= screen_height:
            self.y = new_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)