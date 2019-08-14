import pyxel
from random import *

# ===== Constant =====
HORIZONTAL_Y = 130
COLLIDE_OFFSET = 5

def init():
    pyxel.init(250, 150, caption='NASU')
    pyxel.load('assets/nasu.pyxres')
    drawBackGround()

def initRingo():
    global ringoX, ringoY
    ringoX = randrange(0, pyxel.width)
    ringoY = 0

def collide(ax:int, ay:int, bx:int, by:int) -> bool:
    """Judge collision between Object A and B
    """
    if (abs(ax - bx) <= 16 - COLLIDE_OFFSET) \
        and (abs(ay - by) <= 16 - COLLIDE_OFFSET):
        return True
    else:
        return False


# ===== draw assets =====
def drawRingo(x, y):
    pyxel.blt(x, y, 0,
              0, 0, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawOrange(x, y):
    pyxel.blt(x, y, 0,
                16, 0, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawRottenRingo(x, y):
    pyxel.blt(x, y, 0,
                32, 0, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawBucket(x, y):
    pyxel.blt(x, y, 0,
                0, 16, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawHiyoko(x, y):
    pyxel.blt(x, y, 0,
                16, 16, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawUribo(x, y):
    pyxel.blt(x, y, 0,
                32, 16, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawBackGround():
    pyxel.blt(0, 0, 1, 0, 0, 250, 150)

def drawScore(score:int):
    pyxel.text(10, 142, 'SCORE: {}'.format(score), pyxel.COLOR_WHITE)

def drawAll():
    drawBackGround()
    drawRingo(ringoX, ringoY)
    drawHiyoko(hiyokoX, hiyokoY)
    drawScore(score)
    pyxel.flip()


# ===== sound effects =====
def playSE():
    pyxel.play(0, 0)

def playGameover():
    pyxel.play(0, 1)


# ===== main =====
init()

# variables
hiyokoX = 100
hiyokoY = HORIZONTAL_Y
ringoX = randrange(0, pyxel.width)
ringoY = 0
score = 0

while True:
    # keyboard input
    if pyxel.btn(pyxel.KEY_RIGHT):
        hiyokoX += 4
    if pyxel.btn(pyxel.KEY_LEFT):
        hiyokoX -= 4

    # 当たり判定
    if collide(hiyokoX, hiyokoY, ringoX, ringoY):
        playSE()
        initRingo()
        score += 10

    ringoY += 2
    # 下まで落ちたら戻る
    if ringoY > pyxel.height:
        initRingo()

    # drawAll()
    drawBackGround()
    drawRottenRingo(ringoX, ringoY)
    drawHiyoko(hiyokoX, hiyokoY)
    drawScore(score)
    pyxel.flip()
