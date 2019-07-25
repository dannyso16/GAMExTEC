# ===== Honda janken =====
from PIL import Image
from random import randrange

YOU_WIN_RATE = 50 # 50 %

img_honda    = Image.open('assets/honda.jpg')
img_you_lose = Image.open('assets/you_lose.jpg')
img_you_win  = Image.open('assets/you_win.jpg')

img_honda.show()

if randrange(0,100) >= YOU_WIN_RATE:
    img_you_win.show()
else:
    img_you_lose.show()
