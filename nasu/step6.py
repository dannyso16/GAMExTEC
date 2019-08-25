# 魔法のことば
import pyxel
from random import *
from time import sleep 

# === 定数(途中で値をいじらない予定のもの) =====================
COLLIDE_OFFSET = 5

# === 関数 ===============================================

# 最初にすること
def init():
    pyxel.init(250, 150, caption='NASU')
    pyxel.load('assets/nasu.pyxres')
    drawBackGround()

# りんごの準備
def initFruit():
    global fruitX, fruitY
    fruitX = randrange(0, pyxel.width - 16)
    fruitY = 0

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

# コンボ
def drawCombo(combo:int):
    pyxel.text(10, 132, 'COMBO: {}'.format(combo), pyxel.COLOR_WHITE)
    
# のこり果物
def drawNum(numOfFruits:int):
    pyxel.text(10, 122, 'FRUITS: {}'.format(numOfFruits), pyxel.COLOR_WHITE)

# 画面更新
def drawAll():
    drawBackGround()
    if combo > 0 and combo % 5 == 0:
        drawOrange(fruitX, fruitY)
    else:
        drawRingo(fruitX, fruitY)
    drawHiyoko(hiyokoX, hiyokoY)
    drawScore(score)
    drawCombo(combo)
    drawNum(numOfFruits)
    pyxel.flip()
	
# ========================================================

# 音楽関係
def playSE():
    pyxel.play(0, 0)

def playGameover():
    pyxel.play(0, 1)

def playMiss():
    pyxel.play(0, 2)

# === メイン ===============================================

# ここからスタート！
init()

# 変数
hiyokoX = 100
hiyokoY = 130
initFruit()
score = 0
combo = 0
numOfFruits = 20

while numOfFruits > 0:
    # キーボード入出力
    if pyxel.btn(pyxel.KEY_RIGHT):
        hiyokoX += 4
    if pyxel.btn(pyxel.KEY_LEFT):
        hiyokoX -= 4
    
    if hiyokoX < -16:
        hiyokoX = pyxel.width
    if hiyokoX > pyxel.width:
        hiyokoX = -16
    
    # 当たり判定
    if collide(hiyokoX, hiyokoY, fruitX, fruitY):
        playSE()
        initFruit()
        if combo > 0 and combo % 5 == 0:
            score += 50
        else:
            score += 10
        score += combo
        combo += 1
        numOfFruits -= 1
    
    fruitY += 2
    # 下まで落ちたら戻る
    if fruitY > pyxel.height:
        playMiss()
        initFruit()
        combo = 0
        numOfFruits -= 1
    
    drawAll()

print("Your score is [{}].".format(score))
playGameover()
sleep(4)