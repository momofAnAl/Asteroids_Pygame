# blue.py
import pygame
import random

pygame.init()
pygame.display.set_caption("Kinda Blue")
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((135, 206, 235))
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    r = random.randint(2, 10)
    pygame.draw.circle(screen, (0, 0, 150), (x, y), r)
    pygame.display.flip()
