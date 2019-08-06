import pygame
from pygame.locals import *
import sys
from random import randrange

YOU_WIN_RATE = 1 # 1 %

img_stone    = pygame.image.load('assets/honda_stone.jpg')
img_paper    = pygame.image.load('assets/honda_paper.jpg')
img_scisors  = pygame.image.load('assets/honda_scisors.jpg')
img_you_lose = pygame.image.load('assets/you_lose.jpg')
img_you_win  = pygame.image.load('assets/you_win.jpg')

# TODO: 動画の再生をできないか
# https://qiita.com/miminashi/items/9a2c3f0548e9878145c9
def main():
    your_hand = int(input("ホンダと勝負！！\n何を出す？\nグー：1, チョキ：2, パー：3　："))
    if randrange(0,100) < YOU_WIN_RATE:
        canGetPepsi = True
    else:
        canGetPepsi = False

    pygame.init()
    screen = pygame.display.set_mode((1200, 700))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        show_honda(canGetPepsi, your_hand)
        pygame.display.update()

def show_honda(canGetPepsi, your_hand):
    if canGetPepsi:
        # you win
        if your_hand == 1:
            screen.blit(img_scisors, (0, 0))
        elif your_hand == 2:
            screen.blit(img_paper, (0, 0))
        else:
            screen.blit(img_stone, (0, 0))
    else:
        # you lose
        if your_hand == 1:
            screen.blit(img_paper, (0, 0))
        elif your_hand == 2:
            screen.blit(img_stone, (0, 0))
        else:
            screen.blit(img_scisors, (0, 0))

if __name__ == '__main__':
    main()
