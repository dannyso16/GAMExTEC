import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 700))
image = pygame.image.load('assets/honda_paper.jpg')

def main():
    while True:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        screen.blit(image, (0, 0))
        pygame.display.update()


if __name__ == '__main__':
    main()
