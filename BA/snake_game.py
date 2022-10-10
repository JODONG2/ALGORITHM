import pyautogui as pag 
import time 
i=0
rl = ['right', 'left']
pag.keyDown('command')
pag.keyDown('tab')
pag.keyUp('command')
pag.keyUp('tab')
pag.click()
pag.hotkey('right')
time.sleep(1.6)
pag.hotkey('up')
time.sleep(0.8)
pag.hotkey('left')
#1.93
#가로가 두칸 더 킴 
time.sleep(1.95) # 맨위 
for k in range(1000000):
    pag.hotkey('down')
    if k% 2 == 0 :
        time.sleep(1.77)
    else : 
        time.sleep(1.72)
    pag.hotkey(rl[i])
    i+=1
    time.sleep(2.1)
    for j in range(7):
        pag.hotkey('up',interval=0.0000001)
        pag.hotkey(rl[i%2],interval=0.0000001)
        time.sleep(1.89)
        pag.hotkey('up',interval=0.0000001)
        pag.hotkey(rl[(i+1)%2],interval=0.0000001)
        if(j!=6):
            time.sleep(1.89)
        else:
            time.sleep(2)