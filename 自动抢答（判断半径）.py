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

upper = np.array([0,0,63])
lower = np.array([0,0,36])
# upper = np.array([116,215,208])
# lower = np.array([88,168,174])

# img = cv2.imread('ClassIn_20221124081250.jpg')

# cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
# cv2.namedWindow('bar',cv2.WINDOW_NORMAL)
# cv2.createTrackbar('H_H','bar',0,180,nothing)
# cv2.createTrackbar('S_H','bar',0,255,nothing)
# cv2.createTrackbar('V_H','bar',0,255,nothing)
# cv2.createTrackbar('H_L','bar',0,180,nothing)
# cv2.createTrackbar('S_L','bar',0,255,nothing)
# cv2.createTrackbar('V_L','bar',0,255,nothing)
while 1:
    kbd.wait('ctrl+r')
    stop = 0
    print('开始抢答！')
    while 1:
        # h_h = cv2.getTrackbarPos('H_H','bar')
        # s_h = cv2.getTrackbarPos('S_H','bar')
        # v_h = cv2.getTrackbarPos('V_H','bar')
        # h_l = cv2.getTrackbarPos('H_L','bar')
        # s_l = cv2.getTrackbarPos('S_L','bar')
        # v_l = cv2.getTrackbarPos('V_L','bar')
        
        # upper[0] = h_h
        # upper[1] = s_h
        # upper[2] = v_h
        # lower[0] = h_l
        # lower[1] = s_l
        # lower[2] = v_l

        #获取图像信息
        img = pag.screenshot()
        img = np.array(img)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel=np.ones((5,5),np.uint8))
        # 寻找轮廓
        cnts = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]
        try:  # try尝试语句,防止报错:
            cnt = max(cnts, key=cv2.contourArea)#找到最大的轮廓
            (x1, y1), r = cv2.minEnclosingCircle(cnt)#获取轮廓的x,y坐标，半径参数
            x, y, w, h = cv2.boundingRect(cnt)#获取宽高等参数w,h
            x = int(x1)
            y = int(y1)
            w = int(w)
            h = int(h)
            r = int(r)
            # print('x：{0} y：{1} r：{2} w：{3} h：{4}'.format(x,y,r,w,h))
            # cv2.imshow('mask',mask)
            #鼠标操作 
            if 1270 > y > 240 and 320 < w < 350 and 320 < h < 350:
                pag.click(x, y, clicks=100)
        except:#如果报错则运行下面代码
            r = 0  # Nothing
        
        # !调试计数程序，正常运行请勿启用
        # if 循环次数 <= 100:
        #     循环总时间差 += time.time() - 上一次循环时间戳
        #     上一次循环时间戳 = time.time()
        # elif 循环次数 >= 101:
        #     循环一次平均时间 = 循环总时间差 / 循环次数
        #     print("自动抢答.py")
        #     print("平均每{0}秒循环一次".format(round(循环一次平均时间, 2)))
        #     print("平均1秒点击{0}次".format(round(1 / 循环一次平均时间 * 100)))
        #     break


        
        循环次数 += 1
        kbd.add_hotkey('ctrl+t',out)
        if stop == 1:
            print('停止抢答！')
            break

cv2.destroyAllWindows()

