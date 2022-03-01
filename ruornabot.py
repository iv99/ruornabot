# Бот для Orna RPG GPS Adnroid
# 2022
# iv99
#
# боссы
# крипы
# изображения интерфейса
# botio
# 
#
#
#
from multiprocessing.connection import wait
from random import Random, random
from re import S
import time
from unittest import case
from cv2 import FlannBasedMatcher
import numpy as np
import pyautogui
import pygetwindow
import os
import cv2
GLOBAL_DEBUG = False

class botImgClass:
    def __init__(self,name,dirname) -> None:
        
        self.name = name
        self.img = cv2.imread(dirname + name)
        self.h,self.w,self.d = self.img.shape
        if self.img.size:
            print('Загружаем картинку ' + name + ' из ' + dirname)
        else:
            print('Не загружен файл ' + name + ' из ' + dirname)
        ret,self.mask =cv2.threshold(cv2.bitwise_not(self.img[:,:,1]),1,255,cv2.THRESH_BINARY,)
    def find(self,scr,dex=0.95):
        find = cv2.matchTemplate(scr, self.img, cv2.TM_CCORR_NORMED,mask=self.mask)
        np.nan_to_num(find,False,0.0,0.0,0.0) # сраная магия, убираем inf из результатов
        _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(find,) 
        if (_maxVal > dex):
            if GLOBAL_DEBUG:
                print(self.name,end=' ')
                print('Найден на ',end=' ')
                print(maxLoc,end=' точность ')
                print(_maxVal)
            return (maxLoc[0]+self.w // 2, maxLoc[1]+self.h // 2)
        else:
            if GLOBAL_DEBUG:
                print(self.name,end=' ')
                print('Не найден. макс точность  ',end=' ')
                print(_maxVal)
            return False

class botCreepClass:
    def __init__(self,name,dir) -> None:
        self.img = botImgClass(name,dir)
        self.imgrevert = botImgClass(name,dir)
        self.imgrevert.img = cv2.flip(self.imgrevert.img,1)
        self.imgrevert.mask = cv2.flip(self.imgrevert.mask,1)
    def find(self,src,dex=0.94):
        res1 = self.img.find(src,dex)
        if res1:
            return res1
        else:
            res2 = self.imgrevert.find(src,dex)
            if res2:
                return res2
            else:
                return False



class botClass:
    def __init__(self) -> None:

        self.windId = pygetwindow.getWindowsWithTitle('Bluestacks')[0]
        wind.activate()
        self.refreshScr()

    def click(self,x,y,time=0):
        if (x,y):
            clickx = x + self.windPosX
            clicky = y + self.windPosY
            if time > 0:
                pyautogui.moveTo(clickx,clicky)
                pyautogui.mouseDown()
                cv2.waitKey(time*1000)
                pyautogui.mouseUp()
            else:
                pyautogui.click(clickx,clicky)
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
        self.windId = pygetwindow.getWindowsWithTitle('Bluestacks')[0]
        self.windId.activate()
        #windowActive = self.windId == pygetwindow.getActiveWindow()
        windowActive = True
        if windowActive:
            self.screenWidth,self.screenHeight = pyautogui.size()
            self.windPosX = self.windId.left
            self.windPosY = self.windId.top
            xs,ys = wind.size
            self.scr = pyautogui.screenshot(region=(self.windPosX,self.windPosY,xs,ys))
            self.scr = cv2.cvtColor(np.array(self.scr), cv2.COLOR_RGB2BGR)
            return True
        else:
            print('Ошибка: окно не активно')
            return False

    def display(self,img):
        cv2.imshow('bot',img)
        cv2.waitKey(0)




#function
def loadScreen():
    wind = pygetwindow.getWindowsWithTitle('Bluestacks')[0]
    #wind.activate()
    x,y = pyautogui.size()
    xs,ys = wind.size
    x = wind.left
    y = wind.top
    scr = pyautogui.screenshot(region=(x,y,xs,ys))
    scr = cv2.cvtColor(np.array(scr), cv2.COLOR_RGB2BGR)

    if debug:
        print(">>Скриншот получен")
    return scr

def imgFind(scr,img,dex=0.95):
    find = cv2.matchTemplate(scr,img,cv2.TM_CCORR_NORMED)
    _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(find) 
    #print(cv2.minMaxLoc(find))


    if (_maxVal > dex):
        return maxLoc
    else:
        return False

def Heal(scr):
    cord = imgFind(scr,imgHealBut)
    botClickLong(cord)
    sleep(1)
    return

def botClickLong(cord):
    if cord:
        clickx = cord[0]+clickPos[0]+10
        clicky = cord[1]+clickPos[1]+10
        HealPos = (clickx,clicky)
        
        return True
    else:
        print('Ошибка лонг клик: нет координат')
        return False

def botClick(cord):

    if cord:
        clickx = cord[0]+clickPos[0]+10
        clicky = cord[1]+clickPos[1]+10
        HealPos = (clickx,clicky)
        pyautogui.click(HealPos)
        return True
    else:
        print('Ошибка клик: нет координат')
        return False

def botSwipeUp(cord):

    if cord:
        clickx = cord[0]+clickPos[0]+10
        clicky = cord[1]+clickPos[1]+10
        pyautogui.mouseDown(clickx,clicky)
        pyautogui.move(0,-400)
        pyautogui.mouseUp()
        pyautogui.move(0,400)
        return True
    else:
        print('Ошибка свайпа : нет координат')
        return False

# первая атака
def bot1Attack():
    print('Первая атака')
    clickx = 100+clickPos[0]
    clicky = 650+clickPos[1]
    HealPos = (clickx,clicky)
    pyautogui.click(HealPos)

# Бот боя
def botBattle(cord):
    end = imgFind(scr,imgProdol)
    battle = imgFind(scr,imgChat)
    # Мы в бою?
    end = imgFind(scr,imgProdol)
    if not battle:
        print('Мы не в бою')
        return False
    else:
        print('Мы в бою')
    
    if not end:
        print('Бой не кончен')
    else:
        print('Бой закончен')
    while not end:

        sleep(1)
        bot1Attack()
        sleep(4)  
        scr = loadScreen()
        end = imgFind(scr,imgProdol)
        if not battle:
            print('Мы не в бою')
            return False
        else:
            print('Мы в бою')
    else:
        botClick(end)
        sleep(1)
        botClickLong((800,750))
        sleep(1)
        return True

# Init
debug = False

dirEnemy = 'res\\enemy'
dirBosses = 'res\\bosses'
dirDrops = 'res\\drops'
dirButtons = 'res\\but'

enemy = []
buttons = []
bosses = []
drops = []

enemysDestroyed = 0
imgHealBut = cv2.imread('res\\buttons\\globalHeal.png')
imgProdol = cv2.imread('res\\buttons\\prodol.png')
imgChat = cv2.imread('res\\buttons\\chat.png')
imgClose = cv2.imread('res\\buttons\\krest.png')
imgOrna = cv2.imread('res\\buttons\\ornaBut.png')
imgAttack = cv2.imread('res\\buttons\\attack.png')

clickPos = (0,0)
if pygetwindow.getWindowsWithTitle('Bluestacks'):
    wind = pygetwindow.getWindowsWithTitle('Bluestacks')[0]
    wind.activate()
    x = wind.left
    y = wind.top
    clickPos = (x,y)
else:
    print('Окно не найдено')




# cv2.imshow('glaz',glazimg)
# cv2.waitKey(0)

# glazmask = cv2.bitwise_not(glazimg[:,:,1])
# ret,glazmask2 = cv2.threshold(glazmask,1,255,cv2.THRESH_BINARY)


class botEnemyClass:
    def __init__(self,name,dst) -> None:
        if debug:
            print('Загружаем ' + name + ' по ' + dst)
        self.name = name
        self.img = cv2.imread(dst)
        self.imginvert = cv2.flip(self.img,1)
        ret,self.mask = cv2.threshold(cv2.bitwise_not(self.img[:,:,1]),1,255,cv2.THRESH_BINARY,)
        self.maskinvert = cv2.flip(self.mask,1)

    def find(self, imgSource,dex=0.95):

        find = cv2.matchTemplate(imgSource, self.img, cv2.TM_CCORR_NORMED,mask=self.mask)
        findinvert = cv2.matchTemplate(imgSource, self.imginvert, cv2.TM_CCORR_NORMED,mask=self.maskinvert)
       
        np.nan_to_num(find,False,0.0,0.0,0.0)
        np.nan_to_num(findinvert,False,0.0,0,0.0)

    
        _minVal, _maxVal, minLoc, maxLoc = cv2.minMaxLoc(find,) 
        _minVali, _maxVali, minLoci, maxLoci = cv2.minMaxLoc(findinvert) 
        
        if _maxVali > _maxVal:
            _maxVal = _maxVali
            maxLoc = maxLoci
        
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
                print('Не найденб макс точность  ',end=' ')
                print(_maxVal)
            return False





interfacedir = 'res\\buttons\\'

chervonetsBless = botImgClass('chervonetsBless.png',interfacedir)
chervonetsButton = botImgClass('chervonetsButton.png',interfacedir)
fakelBless = botImgClass('fakelBless.png',interfacedir)
fakelButton = botImgClass('fakelButton.png',interfacedir)
monetaBless = botImgClass('monetaBless.png',interfacedir)
monetaButton = botImgClass('monetaButton.png',interfacedir)
udachaBless = botImgClass('udachaBless.png',interfacedir)
udachaDrop = botImgClass('udachaDrop.png',interfacedir)
mudrostBless = botImgClass('mudrostBless.png',interfacedir)
mudrostDrop = botImgClass('mudrostDrop.png',interfacedir)
ravnyhBless = botImgClass('ravnyhBless.png',interfacedir)
ravnyhButton = botImgClass('ravnyhButton.png',interfacedir)

prodolzhitButton = botImgClass('prodol.png',interfacedir)
fullhp = botImgClass('fullhpmp.png',interfacedir)
mainStatusbar = botImgClass('mainStatusbar.png',interfacedir)
healimg = botImgClass('globalHeal.png',interfacedir)
Close = botImgClass('krest.png',interfacedir)
mainUnd1 = botImgClass('mainUnd1.png',interfacedir)
mainUnd1vhod = botImgClass('mainUnd1vhod.png',interfacedir)
mainUnd2scroll = botImgClass('mainUnd2scroll.png',interfacedir)
arenaNext = botImgClass('arenaNext.png',interfacedir)

battleScroll = botImgClass('battleScroll.png',interfacedir)
battleLeave = botImgClass('battleLeave.png',interfacedir)
battleAttack = botImgClass('battleAttack.png',interfacedir)

battleFullHPMP = botImgClass('battleFullHPMP.png',interfacedir)
battleFullMP = botImgClass('battleFullMP.png',interfacedir)
battleFullHP = botImgClass('battleFullHP.png',interfacedir)
battlePredmety = botImgClass('battlePredmety.png',interfacedir)
battleIntBigHPMP = botImgClass('battleIntBigHPMP.png',interfacedir)
battleIntBigHP = botImgClass('battleIntBigHP.png',interfacedir)
battleIntBigMP = botImgClass('battleIntBigMP.png',interfacedir)

androidOrna = botImgClass('androidOrna.png',interfacedir)
androidWhite = botImgClass('androidWhite.png',interfacedir)
AndroidHome = botImgClass('AndroidHome.png',interfacedir)

bot = botClass()

#bot.display(bot.scr)

# wind.activate()
# scr = loadScreen()
#print(wind)
#print(pygetwindow.getActiveWindow())
# i = 11

    #проверяем хп


bosses = []
bossesdir = 'res\\bosses\\'
bossfiles = os.listdir(bossesdir)
for name in bossfiles:
    loadboss = botImgClass(name,bossesdir)
    bosses.append(loadboss)

creeps = []
creepsdir = 'res\\creeps\\'
creepsfiles = os.listdir(creepsdir)
for name in creepsfiles:
    loadcreeps = botCreepClass(name,creepsdir)
    creeps.append(loadcreeps)

timer_und_max = 300
timer_und = time.time()-300
timer_und_scroll_max = 300
timer_und_scroll = time.time()-300

timer_main_und = time.time()-3600
timer_main_und_max = 3600

while(1):
    #cv2.imshow('bot',bot.scr)
    #cv2.waitKey(1000)    
    bot.refreshScr()
    statusbar = mainStatusbar.find(bot.scr,0.98)
    mainscreen = healimg.find(bot.scr,0.98)
    #если мейн
    if mainscreen and statusbar:
        # проверка на хп и баффы

        #хп мп
        hppos = fullhp.find(bot.scr,0.995)
        hip = healimg.find(bot.scr)
        if hppos:
            if GLOBAL_DEBUG:
                print('Лечение не требуется')
        else:
            print('Лечимся')
            bot.click(hip[0],hip[1],1)
            cv2.waitKey(500)

        udacha = udachaBless.find(bot.scr,0.97)
        chervonets = chervonetsBless.find(bot.scr,0.97)
        fakel = fakelBless.find(bot.scr,0.97)
        moneta = monetaBless.find(bot.scr,0.97)
        mudrost = mudrostBless.find(bot.scr,0.97)
        ravnyh = ravnyhBless.find(bot.scr,0.95)
        #если инвертарного бафа нет то юзаем
        if fakel == False or moneta == False or chervonets == False or ravnyh == False:
            print('Бафаемся с инвентаря')
            bot.click(hip[0],hip[1])
            cv2.waitKey(700)
            bot.scroll(500,500)
            bot.scroll(500,500)
            bot.refreshScr()
            if not fakel:
                fakbutpos = fakelButton.find(bot.scr)
                if fakbutpos:
                    bot.click(fakbutpos[0],fakbutpos[1])
                    cv2.waitKey(100)
            if not moneta:
                monetabutpos = monetaButton.find(bot.scr)
                if monetabutpos:
                    bot.click(monetabutpos[0],monetabutpos[1])
                    cv2.waitKey(100)
            if not chervonets:
                chervonetsbutpos = chervonetsButton.find(bot.scr)
                if chervonetsbutpos:
                    bot.click(chervonetsbutpos[0],chervonetsbutpos[1])
                    cv2.waitKey(100)
            if not ravnyh:
                ravnyhbutpos = ravnyhButton.find(bot.scr)
                if ravnyhbutpos:
                    bot.click(ravnyhbutpos[0],ravnyhbutpos[1])
                    cv2.waitKey(100)
            closepos = Close.find(bot.scr)
            if closepos:
                bot.click(closepos[0],closepos[1])
            

        #ищем статуи если нет
        if udacha == False or mudrost == False:
            if GLOBAL_DEBUG:
                print('Ищем статуи')
            bot.refreshScr()
            if udacha == False:
                udachaDroppos = udachaDrop.find(bot.scr)
                if udachaDroppos:
                    bot.click(udachaDroppos[0],udachaDroppos[1])
                    cv2.waitKey(2000)
                    prodpos = prodolzhitButton.find(bot.scr)
                    if prodpos:
                        bot.click(prodpos[0],prodpos[1])
                    cv2.waitKey(500)
            if mudrost == False:
                mudrostDroppos = mudrostDrop.find(bot.scr)
                if mudrostDroppos:
                    bot.click(mudrostDroppos[0],mudrostDroppos[1])
                    cv2.waitKey(2000)
                    
                    prodpos = prodolzhitButton.find(bot.scr)
                    if prodpos:
                        bot.click(prodpos[0],prodpos[1])
                    cv2.waitKey(500)

        i = 0 # счетчик для переодического рефреша при сканировании на врагов
        #ищем боссов
        bot.refreshScr()
        if GLOBAL_DEBUG:
            print('Ищем боссов')
        for boss in bosses:
            i+=1
            if i > 4:
                bot.refreshScr()
                i = 0
            bosspos = boss.find(bot.scr)
            if bosspos:
                bot.click(bosspos[0],bosspos[1],1)
                cv2.waitKey(2000)
                bot.refreshScr()
                break
            else:
                continue
        
        # bot.refreshScr()
        # #идем в основной андер каждый час
        # if time.time() - timer_main_und > timer_main_und_max and healimg.find(bot.scr,0.98):
        #     timer_main_und = time.time()
        #     print('идем в основной подз')
        #     statusbar = mainStatusbar.find(bot.scr)
        #     if statusbar:
        #         bot.click(statusbar[0],statusbar[1])
        #         cv2.waitKey(2000)
        #         bot.click(750,100)
        #         cv2.waitKey(3000)
        #         bot.refreshScr()
        #         runpos = mainUnd1vhod.find(bot.scr)
        #         if runpos:
        #             bot.click(runpos[0],runpos[1],1)
        #             cv2.waitKey(1000)
        #             continue
        bot.refreshScr()
        # ищем андер на карте каждые 5 мин
        if time.time() - timer_und > timer_und_max:
            undpos = mainUnd1.find(bot.scr)
            if undpos:
                timer_und = time.time()
                bot.click(undpos[0],undpos[1])
                cv2.waitKey(3000)
                bot.refreshScr()
                runpos = mainUnd1vhod.find(bot.scr)
                if runpos:
                    bot.click(runpos[0],runpos[1],1)
                    cv2.waitKey(1000)
                    continue

        if time.time() - timer_und_scroll > timer_und_scroll_max:
            undpos = mainUnd2scroll.find(bot.scr,0.98)
            if undpos:
                timer_und_scroll = time.time()
                bot.click(undpos[0],undpos[1])
                cv2.waitKey(3000)
                bot.refreshScr()
                if Close.find(bot.scr):
                    bot.scroll(500,500)
                cv2.waitKey(500)
                bot.refreshScr()
                runpos = mainUnd1vhod.find(bot.scr)
                if runpos:
                    bot.click(runpos[0],runpos[1],1)
                    cv2.waitKey(1000)
                    continue
        #ищем крипов если не нашли боссов
        bot.refreshScr()
        # мы все еще на глобале?
        if healimg.find(bot.scr):
            if GLOBAL_DEBUG:
                print('Ищем крипов')
            for creep in creeps:
                i+=1
                if i > 4:
                    bot.refreshScr()
                    i = 0
                creeppos = creep.find(bot.scr)
                if creeppos:
                    bot.click(creeppos[0],creeppos[1],1)
                    cv2.waitKey(2000)
                    bot.refreshScr()
                    break
                else:
                    continue
    else:
        #это экран боя?
        battle = battleScroll.find(bot.scr)
        if battle:
            
            if GLOBAL_DEBUG:
                print('В бою')
            # бой завершен?
            contBattle = prodolzhitButton.find(bot.scr)
            if contBattle == False:
                #мы можем уйти? (кнопки активны)
                active = battleAttack.find(bot.scr,0.99)
                if active:
                    if GLOBAL_DEBUG:
                        print('Кнопки активны')
                    #проверка хп ма и есть предметы
                    # ищем на своей половине экрана
                    # cv2.waitKey(200)
                    # bot.refreshScr
                    x,y,z =bot.scr.shape
                    halfscr = bot.scr[0:x, 0:y//2]
                    #bot.display(halfscr)

                    needheal = battleFullHPMP.find(halfscr,0.99)
                    predmetypos = battlePredmety.find(bot.scr)

                    if needheal == False and predmetypos != False:
                        print('требуется пить')
                        

                        heal = battleFullHP.find(halfscr,0.99)
                        mp = battleFullMP.find(halfscr,0.99)

                        bot.click(predmetypos[0],predmetypos[1])
                        cv2.waitKey(300)
                        bot.refreshScr()
                        timewaitheal = 700
                        #хиляемся в зависимости от статуса
                        if heal == False and mp == False:
                            pos = battleIntBigHPMP.find(bot.scr)
                            if pos:
                                bot.click(pos[0],pos[1],1)
                                cv2.waitKey(timewaitheal)
                                bot.refreshScr()
                            else:
                                cls = Close.find(bot.scr)
                                if cls:
                                    bot.click(cls[0],cls[1])
                                cv2.waitKey(300)
                                bot.refreshScr()
                        elif heal == False:
                            pos = battleIntBigHP.find(bot.scr)
                            if pos:
                                bot.click(pos[0],pos[1])
                                cv2.waitKey(timewaitheal)
                                bot.refreshScr()
                            else:
                                cls = Close.find(bot.scr)
                                if cls:
                                    bot.click(cls[0],cls[1])
                                cv2.waitKey(300)
                                bot.refreshScr()
                        elif mp == False:
                            pos = battleIntBigMP.find(bot.scr)
                            if pos:
                                bot.click(pos[0],pos[1])
                                cv2.waitKey(timewaitheal)
                                bot.refreshScr()
                            else:
                                cls = Close.find(bot.scr)
                                if cls:
                                    bot.click(cls[0],cls[1])
                                cv2.waitKey(300)
                                bot.refreshScr()
                    else:
                        print('пить не требуется')
                    randattack = Random()
                    rand = randattack.randint(1,5)
                    if rand == 1:
                        bot.click(1100,650)
                        cv2.waitKey(300)  
                        bot.click(200,420)  
                    elif rand == 2:
                        bot.click(1100,650)
                        cv2.waitKey(300)  
                        bot.click(900,420) 
                    elif rand == 3:
                        bot.click(1100,650)
                        cv2.waitKey(300)  
                        bot.click(1200,420) 
                    elif rand == 4:
                        bot.click(1100,650)
                        cv2.waitKey(300)  
                        bot.click(200,490) 
                    elif rand == 5:
                        bot.click(1100,650)
                        cv2.waitKey(300)  
                        bot.click(900,420) 
                    
                    cv2.waitKey(2000)
                else:
                    if GLOBAL_DEBUG:
                        print('Кнопки не активны')
                    
                    # если потерялись то крест
                    exclose = Close.find(bot.scr)
                    if exclose:
                        bot.click(exclose[0],exclose[1])
                        cv2.waitKey(500)
                    #неактивны, ждем
                    cv2.waitKey(1)
            else:
                # бой завершен жмем кнопку продолжить
                bot.click(contBattle[0],contBattle[1])
                cv2.waitKey(1500)
        else:
            print('Мы потерялись, ищем закрыть или продолжить')
            bot.refreshScr()
            nextcont = arenaNext.find(bot.scr)
            if nextcont:
                bot.click(nextcont[0],nextcont[1])
                cv2.waitKey(1000)
            excont = prodolzhitButton.find(bot.scr)
            if excont:
                bot.click(excont[0],excont[1])
                cv2.waitKey(1000)
            exclose = Close.find(bot.scr)
            if exclose:
                bot.click(exclose[0],exclose[1])
                cv2.waitKey(1000)
            aOrna = androidOrna.find(bot.scr)
            aWhite = androidWhite.find(bot.scr)

            if aOrna != False or aWhite != False:
                if aWhite:
                    hclick = AndroidHome.find(bot.scr)
                    bot.click(hclick[0],hclick[1])
                    cv2.waitKey(1000)
                    bot.refreshScr()
                    aOrna = androidOrna.find(bot.scr)
                if aOrna:
                    bot.click(aOrna[0],aOrna[1])
                    cv2.waitKey(5000)
            bot.refreshScr()
            # закрыть или выйти
            # мы неизвестно где
            pass
print('Конец скрипта')