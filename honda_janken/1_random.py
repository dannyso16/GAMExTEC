# ===== tutrial =====
from random import randrange

YOU_WIN_RATE = 50 # 50 %
if randrange(0,100) >= YOU_WIN_RATE:
    print('YOU WIN')
else:
    print('YOU LOSE')
