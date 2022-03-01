import numpy as np
import pyautogui
import pygetwindow
import os
import cv2

class botImgClass:
    def __init__(self,name,dirname) -> None:
        print('Загружаем картинку' + name + ' из ' + dirname)
        self.name = name
        self.img = cv2.imread(dirname + name)
        ret,self.mask =cv2.threshold(cv2.bitwise_not(self.img[:,:,1]),1,255,cv2.THRESH_BINARY,)
    def find(self,scr,dex=0.95):
        find = cv2.matchTemplate(scr, self.img, cv2.TM_CCORR_NORMED,mask=self.mask)
        np.nan_to_num(find,False,0.0,0.0,0.0) # сраная магия, убираем inf из результатов
        _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(find,) 
        if (_maxVal > dex):
            if debug:
                print(self.name,end=' ')
                print('Найден на ',end=' ')
                print(maxLoc,end=' точность ')
                print(_maxVal)
            return (maxLoc[0]+10, maxLoc[1]+10)
        else:
            if debug:
                print(self.name,end=' ')
                print('Не найден. макс точность  ',end=' ')
                print(_maxVal)
            return False

class botCreepClass:
    def __init__(self,location) -> None:
        self.img = 0
        


class botBossClass:
    pass


class botClass:
    def __init__(self) -> None:
        creeps = []
        bosses = []
        self.scr = 0
        self.refreshScr()

    def click(self,x,y,time=0):
        if (x,y):
            clickx = x + self.windPosX
            clicky = y + self.windPosY
            pyautogui.click(clickx,clicky,duration=time)
            return True
        else:
            print("Ошибка: нет координат")

    def scroll(self,x,y):
        if (x,y):
            clickx = x + self.windPosX + 10
            clicky = y + self.windPosY + 10
            pyautogui.mouseDown(clickx,clicky)
            pyautogui.move(0,-400)
            pyautogui.mouseUp()
            pyautogui.move(0,400)
            return True
        else:
            print('Ошибка свайпа : нет координат')
            return False

    def refreshScr(self):
            wind = pygetwindow.getWindowsWithTitle('Bluestacks')[0]
            wind.activate()
            self.screenWidth,self.screenHeight = pyautogui.size()
            self.windPosX = wind.left
            self.windPosY = wind.top
            x = wind.left
            y = wind.top
            xs,ys = wind.size
            self.scr = pyautogui.screenshot(region=(x,y,xs,ys))
            self.scr = cv2.cvtColor(np.array(self.scr), cv2.COLOR_RGB2BGR)
            return True

    def display(self,img):
        cv2.imshow('bot',img)
        cv2.waitKey(0)


bot = botClass()

bot.display(bot.scr)

# это главный
