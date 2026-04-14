import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball = Ball(WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    dx, dy = 0, 0

    if keys[pygame.K_UP]:
        dy = -ball.speed
    if keys[pygame.K_DOWN]:
        dy = ball.speed
    if keys[pygame.K_LEFT]:
        dx = -ball.speed
    if keys[pygame.K_RIGHT]:
        dx = ball.speed

    # движение каждый кадр
    ball.move(dx, dy, WIDTH, HEIGHT)

    screen.fill((255, 255, 255))
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()