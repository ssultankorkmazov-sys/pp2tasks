import pygame

pygame.init()


def get_images():
    clock_img = pygame.image.load(r"C:\Users\user\pp2\practice_9\mickeys_clock\images\chasy.jpg").convert()
    left_hnd = pygame.image.load(r"C:\Users\user\pp2\practice_9\mickeys_clock\images\Mickey_hand.png").convert_alpha()
    right_hnd = pygame.image.load(r"C:\Users\user\pp2\practice_9\mickeys_clock\images\Mickey_sec.png").convert_alpha()
    
    return clock_img, left_hnd, right_hnd