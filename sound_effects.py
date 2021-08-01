import pygame

pygame.mixer.init()

# Load the sounds in Target Practice.
bullet_fire = pygame.mixer.Sound('sounds/bullet_fire.wav')
target_hit = pygame.mixer.Sound('sounds/target_hit.wav')
target_miss = pygame.mixer.Sound('sounds/target_miss.wav')