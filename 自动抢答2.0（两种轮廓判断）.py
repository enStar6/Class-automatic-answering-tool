import cv2, numpy as np, pyautogui as pag, time, keyboard as kbd

pag.PAUSE = 0

def nothing(x):
    pass
def out():
    global stop
    stop = 1

stop = 0
循环次数 = 0
循环一次平均时间 = 0
上一次循环时间戳 = time.time()
循环总时间差 = 0

upper1 = np.array([0,0,63])
lower1 = np.array([0,0,36])
upper2 = np.array([126,54,184])
lower2 = np.array([105,7,57])
find = 0

while 1:
    kbd.wait('ctrl+r')
    stop = 0
    print('自动抢答，点击四！')
    while 1:
        #获取图像信息
        img = pag.screenshot()
        img = np.array(img)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, lower1,upper1)
        mask2 = cv2.inRange(hsv, lower2,upper2)
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, kernel=np.ones((5,5),np.uint8))
        mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernel=np.ones((5,5),np.uint8))
        # 寻找轮廓
        cnts1= cv2.findContours(mask1.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
        cnts2= cv2.findContours(mask2.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
        try:  # try尝试语句,防止报错:
            for cnt2 in cnts2:
                (xc2, yc2), r2 = cv2.minEnclosingCircle(cnt2)#获取轮廓的x,y坐标，半径参数
                xt2, yt2, w2, h2 = cv2.boundingRect(cnt2)#获取宽高等参数w,h
                xc2 = int(xc2)
                yc2 = int(yc2)
                r2 = int(r2)
                w2 = int(w2)
                h2 = int(h2)

                if 1250 > yc2 > 350 and 260 < w2 < 280 and 260 < h2 < 280:
                    pag.click(xc2, yc2, clicks=100)
                    find = 1
                    break
            if find != 1:
                for cnt1 in cnts1:
                    (xc1, yc1), r1 = cv2.minEnclosingCircle(cnt1)#获取轮廓的x,y坐标，半径参数
                    xtq, ytq, w1, h1 = cv2.boundingRect(cnt1)#获取宽高等参数w,h
                    xc1 = int(xc1)
                    yc1 = int(yc1)
                    r1 = int(r1)
                    w1 = int(w1)
                    h1 = int(h1)

                    if 1270 > yc1 > 240 and 330 < w1 < 350 and 330 < h1 < 350:
                        pag.click(xc1, yc1, clicks=100)
                        break

        except:#如果报错则运行下面代码
            pass

        循环次数 += 1
        kbd.add_hotkey('ctrl+t',out)
        if stop == 1:
            print('不要抢答！不要抢答！不要抢答！')
            break

cv2.destroyAllWindows()