# zoomzoom.py
import pygame

pygame.init()
pygame.display.set_caption("ZoomZoom")

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pos = 0
direction = 1
speed = 20
fps = 30
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed += 1
            if event.key == pygame.K_LEFT and speed > 0:
                speed -= 1
            if event.key == pygame.K_UP:
                fps += 1
            if event.key == pygame.K_DOWN and fps > 1:
                fps -= 1

            print(f"Speed: {speed} @ FPS: {fps}")

    pos += direction * speed
    if pos <= 0:
        pos = 0
        direction = 1
    elif pos > width:
        pos = width
        direction = -1

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (pos, 300), 5)
    pygame.display.flip()

    clock.tick(fps)