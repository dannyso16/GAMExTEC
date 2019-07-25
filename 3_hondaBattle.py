# ===== Honda janken =====
from PIL import Image
from random import randrange

YOU_WIN_RATE = 1 # 1 %

img_stone    = Image.open('assets/honda_stone.jpg')
img_paper    = Image.open('assets/honda_paper.jpg')
img_scisors  = Image.open('assets/honda_scisors.jpg')
img_you_lose = Image.open('assets/you_lose.jpg')
img_you_win  = Image.open('assets/you_win.jpg')

your_hand = int(input('ホンダと勝負！！\n何を出す？\nグー：1, チョキ：2, パー：3　：'))
if randrange(0,100) < YOU_WIN_RATE:
    canGetPepsi = True
else:
    canGetPepsi = False

if canGetPepsi:
    # you win
    img_you_win.show()
    if your_hand == 1:
        img_scisors.show()
    elif your_hand == 2:
        img_paper.show()
    else:
        img_stone.show()
else:
    # you lose
    img_you_lose.show()
    if your_hand == 1:
        img_paper.show()
    elif your_hand == 2:
        img_stone.show()
    else:
        img_scisors.show()
