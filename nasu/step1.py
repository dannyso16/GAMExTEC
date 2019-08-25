# 魔法のことば
import pyxel
from random import *

# === 定数(途中で値をいじらない予定のもの) =====================
COLLIDE_OFFSET = 5

# === 関数 ===============================================

# 最初にすること
def init():
    pyxel.init(250, 150, caption='NASU')
    pyxel.load('assets/nasu.pyxres')
    drawBackGround()

# りんごの準備
def initRingo():
    global ringoX, ringoY
    ringoX = randrange(0, pyxel.width - 16)
    ringoY = 0

# 当たり判定
def collide(ax:int, ay:int, bx:int, by:int) -> bool:
    """Judge collision between Object A and B
    """
    if (abs(ax - bx) <= 16 - COLLIDE_OFFSET) \
        and (abs(ay - by) <= 16 - COLLIDE_OFFSET):
        return True
    else:
        return False

# りんご
def drawRingo(x, y):
    pyxel.blt(x, y, 0,
              0, 0, 16, 16, pyxel.COLOR_LIGHTGRAY)

# みかん
def drawOrange(x, y):
    pyxel.blt(x, y, 0,
                16, 0, 16, 16, pyxel.COLOR_LIGHTGRAY)

# かご
def drawBucket(x, y):
    pyxel.blt(x, y, 0,
                0, 16, 16, 16, pyxel.COLOR_LIGHTGRAY)

# ひよこ
def drawHiyoko(x, y):
    pyxel.blt(x, y, 0,
                16, 16, 16, 16, pyxel.COLOR_LIGHTGRAY)

# うりぼー
def drawUribo(x, y):
    pyxel.blt(x, y, 0,
                32, 16, 16, 16, pyxel.COLOR_LIGHTGRAY)

# 背景
def drawBackGround():
    pyxel.blt(0, 0, 1, 0, 0, 250, 150)

# 得点
def drawScore(score:int):
    pyxel.text(10, 142, 'SCORE: {}'.format(score), pyxel.COLOR_WHITE)

# --- ここから上はいじらないで！ ---

# 画面更新
def drawAll():
    drawBackGround()
    pyxel.flip()
	
# ========================================================

# 音楽関係
def playSE():
    pyxel.play(0, 0)

def playGameover():
    pyxel.play(0, 1)

# === メイン ===============================================

# ここからスタート！
init()

# 変数
hiyokoX = 0
hiyokoY = 0

while True:
    drawAll()