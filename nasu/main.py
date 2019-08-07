import pyxel
from random import *

# ===== Constant =====
HORIZONTAL_Y = 130

# TODO: 関数をutilsにわける
def init():
    pyxel.init(250, 150, caption='NASU')
    pyxel.load('assets/nasu.pyxres')
    drawBackGround()

# TODO: 当たり判定の関数をつくる
# 膝神へ　引数どうしましょ
def collide():
    pass


# ===== draw assets =====
def drawRingo(x, y):
    pyxel.blt(x, y, 0,
              0, 0, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawOrange(x, y):
    pyxel.blt(x, y, 0,
                16, 0, 16, 16, pyxel.COLOR_LIGHTGRAY)

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


# ===== sound effects =====
def playSE():
    pyxel.play(0, 0)

def playGameover():
    pyxel.play(0, 1)


# ===== main =====
init()

# variables
hiyokoX = 100
ringoX = 100 # TODO: ランダム性の導入
ringoY = 0
score = 0

playGameover() # sound test

while True:
    if pyxel.btn(pyxel.KEY_RIGHT):
        hiyokoX += 5
    if pyxel.btn(pyxel.KEY_LEFT):
        hiyokoX -= 5
    # TODO: 当たり判定
    # TODO: リンゴが落ちて上に戻る処理

    drawBackGround()
    drawHiyoko(hiyokoX, HORIZONTAL_Y)
    # TODO: リンゴの落下
    pyxel.flip()
