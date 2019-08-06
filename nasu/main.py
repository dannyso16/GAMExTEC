import pyxel

# ===== Constant =====
HORIZONTAL_Y = 130

# TODO: 関数をutilsにわける
def init():
    pyxel.init(250, 150, caption='NASU')
    pyxel.load('assets/nasu.pyxres')
    drawBackGround()

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
# TODO: ひざ神　動作確認してちょ
def playSE():
    pyxel.play(0, 0)

def playGameover():
    pyxel.play(1, 0)


# ===== main =====
init()

drawHiyoko(100, HORIZONTAL_Y)
drawRingo(120, 40)
drawScore(100)
pyxel.show()
