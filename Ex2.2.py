import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Figure One")

YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)


win.fill(WHITE)
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        pygame.draw.circle(win, BLACK,(300,300),200,0)
        pygame.draw.rect(win, YELLOW, (195, 195, 210, 210))

    pygame.display.update()