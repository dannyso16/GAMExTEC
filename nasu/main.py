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
    anim_frame_count = pyxel.frame_count // 3
    idx = anim_frame_count % 4 # animation has 4 images
    pyxel.blt(x, y, 0,
                idx*16, 32, 16, 16, pyxel.COLOR_LIGHTGRAY)

def drawUribo(x, y):
    anim_frame_count = pyxel.frame_count // 3
    idx = anim_frame_count % 4 # animation has 4 images
    sign = -1 if isLookingLeft else 1
    pyxel.blt(x, y, 0,
                idx*16, 48, sign*16, 16, pyxel.COLOR_LIGHTGRAY)

def drawBackGround(earthQuake=False):
    CLOUD_OFFSET = 56 # the maximum width of clouds
    anim_frame_count = pyxel.frame_count // 3

    # Three clouds move left to right side
    # when clouds come to the right edge, transfer it to the left edge
    mod = (pyxel.width + CLOUD_OFFSET)
    cloud1X = anim_frame_count       % mod - CLOUD_OFFSET
    cloud2X = (anim_frame_count-100) % mod - CLOUD_OFFSET
    cloud3X = (anim_frame_count-180) % mod - CLOUD_OFFSET

    pyxel.cls(pyxel.COLOR_CYAN)
    pyxel.blt(cloud1X,  8,  1, 16,  8, 56, 32)
    pyxel.blt(cloud2X,  16, 1, 192, 8, 48, 32)
    pyxel.blt(cloud3X,  10, 1, 16,  8, 56, 32)

    amplitude = anim_frame_count%2 if earthQuake else 0
    pyxel.blt(0, 48+amplitude, 1, 0, 48, 250, 150) # ground and trees

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
isLookingLeft = True

while True:
    # keyboard input
    if pyxel.btn(pyxel.KEY_RIGHT):
        hiyokoX += 4
        isLookingLeft = True
    if pyxel.btn(pyxel.KEY_LEFT):
        hiyokoX -= 4
        isLookingLeft = False

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
    drawRingo(ringoX, ringoY)
    drawHiyoko(hiyokoX, hiyokoY)
    drawScore(score)
    pyxel.flip()
