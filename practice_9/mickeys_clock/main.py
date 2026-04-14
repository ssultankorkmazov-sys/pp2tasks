import pygame
import datetime
from clock import get_images

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

clock_img, left_hnd, right_hnd = get_images()

clock_img = pygame.transform.smoothscale(clock_img, (500, 500))
left_hnd = pygame.transform.smoothscale(left_hnd, (60, 120))
right_hnd = pygame.transform.smoothscale(right_hnd, (60, 120))

#center
rect = clock_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
center = rect.center

#originals
orig_left = left_hnd
orig_right = right_hnd

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    #background
    screen.blit(clock_img, rect)

    # time
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    # angle 
    sec_angle = -seconds * 6
    min_angle = -(minutes + seconds / 60) * 6

    #rotation 
    left_rot = pygame.transform.rotate(orig_left, min_angle)
    right_rot = pygame.transform.rotate(orig_right, sec_angle)
    left_rot.set_alpha(150)
    #centre 
    left_rect = left_rot.get_rect(center=center)
    right_rect = right_rot.get_rect(center=center)

    # drawing 
    screen.blit(right_rot, right_rect)
    screen.blit(left_rot, left_rect)

    pygame.draw.circle(screen, (255, 0, 0), center, 4)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()