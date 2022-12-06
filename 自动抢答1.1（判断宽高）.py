import cv2, numpy as np, pyautogui as pag, time, keyboard as kbd

pag.PAUSE = 0

stop = 0
循环次数 = 0
循环一次平均时间 = 0
上一次循环时间戳 = time.time()
循环总时间差 = 0

def nothing(x):
    pass
def out():
    global stop
    stop = 1

upper = np.array([0,0,63])
lower = np.array([0,0,36])
# upper2 = np.array([126,54,184])
# lower2 = np.array([105,7,57])
find = 0

while 1:
    kbd.wait('ctrl+r')
    stop = 0
    print('给抢答以文明，给外挂以生命！')
    while 1:
        #获取图像信息
        img = pag.screenshot()
        img = np.array(img)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower,upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel=np.ones((5,5),np.uint8))   
        cnts= cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
        try:
            for cnt in cnts:
                (xc, yc), r = cv2.minEnclosingCircle(cnt)#获取轮廓的x,y坐标，半径参数
                xt, yt, w, h = cv2.boundingRect(cnt)#获取宽高等参数w,h
                xc = int(xc)
                yc = int(yc)
                r = int(r)
                w = int(w)
                h = int(h)

                if 1270 > yc > 240 and 320 < w < 350 and 320 < h < 350:
                    pag.click(xc, yc, clicks=100)
                    find = 1
                    break
        except:
            print('未找到目标轮廓')
        
        循环次数 += 1
        kbd.add_hotkey('ctrl+t',out)
        if stop == 1:
            print('不要抢答！不要抢答！不要抢答！')
            break
cv2.destroyAllWindows()
