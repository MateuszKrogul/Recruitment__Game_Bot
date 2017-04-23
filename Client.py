#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nazwa pliku: zmienne.py
# -> Write function to check if you can collect the good
#   if not then get time to end task then wait 
#   after that try collect again

# 1)    Na każdym elemencie odpalaj checkIfResponding.
#       Jeżeli element nie odpowiadał i zacznie odpowiadać
#       to przejdź do strony startowej i zacznij robić
#       to co robiłeś.
# '//*[@id="dialogContainer"]/div/div[3]/div[2]/div' zamknięcie reklamy 'zapraszaj znajomych'
# class = titleBarControl wclose

import selenium
from threading import Thread
import thread
import threading
import pickle
import time
import traceback
import inspect
import logging 
import math
import os.path
import errno 
from datetime import datetime
from selenium import webdriver
from random import uniform
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.common.keys import Keys


# ktos atakuje spy '//*[@id="eventPanelEntry2632755"]/div/div[1]/div[1]/div[2]/div[1]/span[1]'
def get_function_name():
    return traceback.extract_stack(None, 2)[0][2]

def get_codeline():
   stack = traceback.extract_stack()
   filename, codeline, funcName, text = stack[-2]
   return codeline 

def CP(nr):
    logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values() + " TO TUTAJ !!! CP" + str(nr))

def get_function_parameters_and_values():
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    argsAndValues = "("
    for i in args:
        if(i == "self"):
            continue
        if(type(values[i]) == type(u"")): value = values[i].encode("utf-8")
        else: value = str(values[i])
        if(i == args[len(args)-1]):
            argsAndValues += i + "=" + value + ")"
            break
        argsAndValues += i + "=" + value + ","
    return argsAndValues

def closeProgram(t):
    logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
    while(True):
        if(time.strftime("%H:%M:%S") > t):
            toPrint = "Zamykam o " + time.strftime("%H:%M:%S")
            self.saveToShortLog(toPrint)
            print(toPrint)
            mb.sendMessage(toPrint)
            thread.interrupt_main()
            break
        time.sleep(1)

def rnd(a,b):
    '''Przerwa trwająca <a,b>.'''
    logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
    time.sleep(round(uniform(a,b),4))  

class Bot:
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    )
    #br = webdriver.PhantomJS(desired_capabilities=dcap)
    #br.maximize_window()
    #br = webdriver.Chrome()
    #br.set_window_size(1200, 740)
    br = None
    isLogged = False
    isTaskStopped = False
    isBarbariansAttacked = False
    isKeyboardInterrupt = False

    def __init__(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        self.loadProgramData()

    def test(self, isTest):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        if(isTest):
            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            chrome_options.add_experimental_option("prefs",prefs)
            self.br = webdriver.Chrome(chrome_options=chrome_options)
            self.br.set_window_size(1200, 740)
        else:
            self.br = webdriver.PhantomJS(desired_capabilities=self.dcap)
            self.br.maximize_window()    

    def c(self, xPath):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        '''Klika element podany jako arkugemnt.'''
        self.waitForVisibility(xPath)
        logging.debug("After waitForPresence() in " + get_function_name() + "(). Line: " + str(get_codeline()-1))
        self.elem(xPath).click()
        logging.debug("After elem() in " + get_function_name() + "(). Line: " + str(get_codeline()-1))            

    def v(self, xPath, value):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        '''Zmienia wartość atrybutu podanego jako argument'''
        self.waitForVisibility(xPath)
        elem = self.elem(xPath)
        elem.clear()
        elem.send_keys(value)

    def exist(self, xPath):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        '''Sprawdza czy element istnieje.'''
        try:

            self.br.find_element_by_xpath(xPath)
        except NoSuchElementException:

            return False

        return True 

    def elemExist(self,elem, xPath):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        try:
            elem.find_element_by_xpath(xPath)
            
        except NoSuchElementException:
            
            return False
            
        return True

    def login(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        '''Logowanie.'''
        self.v(".//*[@id='loginUsername']","piruet")
        if(self.isTaskStopped): return
        #rnd(1,2)
    	
    	# Security hidden
        self.v(".//*[@id='loginPassword']","*************************")
        if(self.isTaskStopped): return
        #rnd(1,2)
    
        self.c(".//*[@id='loginServer']")
        if(self.isTaskStopped): return
        #rnd(1,2)
    
        self.c(".//*[@id='loginServer']/option[2]")
        if(self.isTaskStopped): return
        #rnd(1,2)
        
        self.c(".//*[@id='loginSubmit']")
        if(self.isTaskStopped): return
        #rnd(1,2)
        self.isLogged = True

    def move(self, city):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        e = self.br.find_element_by_xpath(".//*[@id='citymapContent']/map/area[6]")
        el = self.br.find_element_by_xpath(".//*[@id='citymapContent']/map/area[13]")
    
        if(city == "city3" or city == "city4" or city == "city5"):
            e = self.br.find_element_by_xpath(".//*[@id='citymapContent']/map/area[7]")
            el = self.br.find_element_by_xpath(".//*[@id='citymapContent']/map/area[14]")
        a = ActionChains(self.br)
        a.move_to_element(e).perform()
        a.click_and_hold(e).perform()
        a.move_to_element(el).perform()
        time.sleep(2)
        #a.release().perform()

    def selectCity(self, city):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        #TODO add xPAths to cities 
        cities = {  "city1" : "//*[@id='citySelector']/div[2]/ul/li[1]",
                    "city2" : "//*[@id='citySelector']/div[2]/ul/li[2]",
                    "city3" : "//*[@id='citySelector']/div[2]/ul/li[3]",
                    "city4" : "//*[@id='citySelector']/div[2]/ul/li[4]",  
                    "city5" : "//*[@id='citySelector']/div[2]/ul/li[5]"  
                }
        xPath = "//*[@id='citySelector']/div[1]/div[3]"
        self.c(xPath)
        self.c(cities[city])

        self.br.refresh()
        xPath = "//*[@id='citymapContent']/map/area[1]"
        self.waitXpath(xPath, 10, True)
        self.waitForVisibility(xPath)

    def collect(self, material, city):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        #kukurydza
        corn =  [   '//*[@id="citymapContent"]/map/area[5]',
                    ".//*[@id='CornFarmBwindowRightAFootContent']/div[2]/div[2]/div[1]/div[3]",
                    ".//*[@id='CornFarmBwindowRightAFootContent']/div[2]/div[4]/button",
                    ".//*[@id='CornFarmBwindowRightAFootContent']/div[1]/div[1]/div/div/div[2]/button",
                    ".//*[@id='dialogContainer']/div/div[3]/div[2]/div",
                    '//*[@id="CornFarmBwindowBuildingName"]'  
                ]
        limestone = [   ".//*[@id='citymapContent']/map/area[2]",
                        ".//*[@id='QuarryBwindowRightAFootContent']/div[2]/div[2]/div[1]/div[3]",
                        ".//*[@id='QuarryBwindowRightAFootContent']/div[2]/div[4]/button",
                        ".//*[@id='QuarryBwindowRightAFootContent']/div[1]/div[1]/div/div/div[2]/button",
                        ".//*[@id='dialogContainer']/div/div[3]/div[2]/div",
                        '//*[@id="QuarryBwindowBuildingName"]'
                ]
        obsidian =  [   ".//*[@id='citymapContent']/map/area[3]",
                        ".//*[@id='ObsidianMineBwindowRightAFootContent']/div[2]/div[2]/div[1]/div[3]",
                        ".//*[@id='ObsidianMineBwindowRightAFootContent']/div[2]/div[4]/button",
                        ".//*[@id='ObsidianMineBwindowRightAFootContent']/div[1]/div[1]/div/div/div[2]/button",
                        ".//*[@id='dialogContainer']/div/div[3]/div[2]/div",
                        '//*[@id="ObsidianMineBwindowBuildingName"]'  
                    ]
        cocoa = [   ".//*[@id='citymapContent']/map/area[4]",
                    ".//*[@id='CacaoPlantationBwindowRightAFootContent']/div[2]/div[2]/div[1]/div[3]",
                    ".//*[@id='CacaoPlantationBwindowRightAFootContent']/div[2]/div[4]/button",
                    ".//*[@id='CacaoPlantationBwindowRightAFootContent']/div[1]/div[1]/div/div/div[2]/button",
                    ".//*[@id='dialogContainer']/div/div[3]/div[2]/div" ,
                    '//*[@id="CacaoPlantationBwindowBuildingName"]' 
                ]
            
        materials =     {   "corn"      :   corn,
                            "limestone" :   limestone,
                            "obsidian"  :   obsidian,
                            "cocoa"     :   cocoa
                        }
         
        if(city == "city1" or city == "city2"):
            corn[0]         = ".//*[@id='citymapContent']/map/area[5]"
            limestone[0]    = ".//*[@id='citymapContent']/map/area[2]"
            obsidian[0]     = ".//*[@id='citymapContent']/map/area[3]"
            cocoa[0]        = ".//*[@id='citymapContent']/map/area[4]"  
                     
        if(city == "city3" or city == "city4" or city == "city5"):
            corn[0]         = ".//*[@id='citymapContent']/map/area[6]"
            limestone[0]    = ".//*[@id='citymapContent']/map/area[3]"
            obsidian[0]     = ".//*[@id='citymapContent']/map/area[4]"
            cocoa[0]        = ".//*[@id='citymapContent']/map/area[5]"
         
        if(material == "cocoa"): ActionChains(self.br).release().perform()   
        xPath = '//*[@id="dialogContainer"]/div/div[2]/div'
        if(self.exist(xPath)):
            elem = self.elem(xPath)
            if(elem.text == "Magazyn"):
                xPath = '//*[@id="dialogContainer"]/div/div[3]/div[2]/div'
                self.c(xPath)
                self.waitXpath(xPath, 5 , False)
                
        
        self.c(materials[material][0])
        
        
            
        self.waitForVisibility(materials[material][5])
        self.waitForPresence(materials[material][5])
        if(self.isTaskStopped): return
        #rnd(2,3)
        
        if(self.exist(materials[material][1]) == True):
            #nie dawać waitForVisibility bo elem nie widać
            elem = self.waitForPresence(materials[material][1])
            if(elem.text != ""):
                self.waitForVisibility(materials[material][1])
                t = self.waitForPresence(materials[material][1])
            
                if(self.isTaskStopped): return
                t = t.text
                #t = b.br.find_element_by_xpath(materials[material][1]).text
                if(t != "Gotowe"):
                    #self.updateActivePlayers(city)
                    if(time.strftime("%H:%M") < "05:00" and self.isBarbariansAttacked == True): self.isBarbariansAttacked = False
                    if(time.strftime("%H:%M") > "05:00" and self.isBarbariansAttacked == False):
                        self.selectCity("city1") 
                        self.findBarbarians()
                        toPrint = "Barabians attacked"
                        self.saveToShortLog(toPrint)
                        print(toPrint)
                        mb.sendMessage(toPrint)
                        self.isBarbariansAttacked = True
                        xPath = '//*[@id="menuLinkCity"]/div[2]'
                        self.c(xPath)
                        xPath = '//*[@id="citymapContent"]/map/area[1]'
                        self.waitForVisibility(xPath)
                        self.waitForPresence(xPath)
                    
                        self.selectCity(city)
                        self.collect(material, city)
                        return
                    Bot.working = True
                    Bot.seconds = 1
                    Bot.minutes = 1

                    def countDown(t):
                        t = t[11:]
                        hours = int(t[:2])
                        minutes = int(t[3:5])
                        seconds = int(t[6:8])
        
                        bonusTime = int(round(uniform(10,40),0))
                        wait = seconds + 60 * minutes + 60 * 60 * hours + bonusTime
    
                        hours = int(round(wait/3600,0))
                        minutes = int(round((wait- hours*3600)/60,0))
                        seconds = int(wait - hours*60*60 - minutes*60)
                        Bot.seconds = seconds
                        Bot.minutes = minutes
                        isFirst = True
                        Bot.quitCountDown = False
                        while(True):
                            if(isFirst == True):
                                toPrint = time.strftime("%H:%M:%S ") + u"Pozostało: " + str(hours) + ":"+ str(minutes) + ":" + str(seconds)
                                self.saveToShortLog(toPrint)
                                print(toPrint)
                                mb.sendMessage(toPrint)
                                isFirst = False 
                            if(seconds == 30 or seconds == 0):
                                toPrint = time.strftime("%H:%M:%S ") + u"Pozostało: " + str(hours) + ":"+ str(minutes) + ":" + str(seconds)
                                self.saveToShortLog(toPrint)
                                print(toPrint)
                                mb.sendMessage(toPrint)
                            time.sleep(1)
                            if(tentlanLoop.isKeyboardInterrupt == True or Bot.quitCountDown == True):
                                Bot.quitCountDown = False
                                logging.debug("Break in " + get_function_name())
                                raise SystemExit
                            if(minutes == 0 and seconds == 0):
                                Bot.working = False
                                logging.debug("0:0 end in " + get_function_name())
                                break
                            if(seconds == 0): 
                                minutes -= 1
                                Bot.minutes -= 1
                                seconds = 59
                                Bot.seconds = 59
                            else:
                                seconds -= 1
                                Bot.seconds -= 1
                    countDownThread = Thread(target= countDown, args=(t,), name="countDownThread")
                    countDownThread.start()
                    while(Bot.working == True):
                        if(Bot.seconds == 30 or Bot.seconds == 0):
                            self.checkIfEnemyAttack()
                            isThreadAlive = False
                            threads = threading.enumerate()
                            for thread in threads:
                                if(thread.getName() == "t1"): isThreadAlive = True
                            if(isThreadAlive == False):
                                pass
                                #t1 = Thread(target=self.checkIfEnemyAttack, name="t1")
                                #t1.start()
                                #t1.join()
                        if(Bot.minutes == 0 and Bot.seconds == 0):
                            xPath = '//*[@id="dialogContainer"]/div/div[2]/div'
                            if(self.exist(xPath) != True):
                                self.c(materials[material][0])
                            break
                        
                    
                    
                #zbierz
                self.c(materials[material][2])
                if(self.isTaskStopped): return
            

        
    
        #produkuj (10min)
        self.c(materials[material][3])
        if(self.isTaskStopped): return

        #zamknij
        self.c(materials[material][4])
        self.waitXpath(materials[material][4], 5, False)
        if(self.isTaskStopped): return

    def checkIfResponding(self, isLogged):
        '''Jeśli strona nie odpowiada to odświeża.'''
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        count = 0
        wait = 60
        while(True):
            if(count == 60): wait = 10 * 60 #raise SystemExit #po godzinie zamyka program
            if(self.br.title == u"Witryna http://pl2.tentlan.com/ jest niedostępna"):
                time.sleep(wait)
                self.br.refresh()
                count += 1
                if(count==1): Bot.isTaskStopped = True
            else:
                if(isLogged):
                    if(count > 0): 
                        self.br.get("http://pl2.tentlan.com/overwiew")
                        break
                    else: break
                else: break

    def updateActivePlayers(self, city):

        def saveActivePlayers(elem):
            logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
            f = open(r'C:\Users\mati\Desktop\Python\tekst.txt', 'w')
            f.write(elem.encode('utf8'))
            f.flush()
            f.close()
            
            path = r'C:\Users\mati\Desktop\Python\ActivePlayersArchive.txt'
            if(os.path.exists(path) != True):
                f = open(path, 'w')
                f.flush()
                f.close()
                
            PlayerList = PlayersOnline().whoIsOnline()
            save = "["
            for i in PlayerList:
                save += i + ", "
            position = str.rfind(save, ",")
            save = list(save)
            save[position] = "]"
            save = "".join(save)
            
            f = open(r'C:\Users\mati\Desktop\Python\ActivePlayersArchive.txt', 'a')
            f.write("\r" + time.strftime('%Y:%m:%d %H:%M:%S ') + "Online: " + str(len(PlayerList)) + " "+ save)
            toPrint = "Active players list updated"
            self.saveToShortLog(toPrint)
            print(toPrint)
            mb.sendMessage(toPrint)

        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        xPath = "//*[@id='dialogContainer']/div/div[3]/div[2]/div"
        if(self.exist(xPath)):
            self.c(xPath)
            self.waitXpath(xPath, 5 , False)

        
        if(self.isTaskStopped == True): return
           
        xPath = "//*[@id='menuLinkWorldmap']/div[2]"
        self.c(xPath)
        if(self.isTaskStopped == True): return
        
        xPath = "//*[@id='mapTile500560-204']"
        self.waitForVisibility(xPath)
        self.waitForPresence(xPath)
        time.sleep(2)
        self.c(xPath)
        
        xPath = "//script[@id='worldmapData']"
        elem = self.br.find_element_by_xpath(xPath)
        elem = elem.get_attribute('innerHTML')
        
        xPath = "//*[@id='mapTile500560-204']"
        #self.br.refresh()
        self.c(xPath)
        #self.screen("AfterClickVillage")
        
        # kliknij home
        # poczekja chwile

        if(self.isTaskStopped == True): return
        
        xPath = "//*[@id='menuLinkCity']/div[2]"
        self.c(xPath)
        if(self.isTaskStopped == True): return
        
        xPath = "//*[@id='citymapContent']/map/area[1]"
        self.waitForVisibility(xPath)
        self.waitForPresence(xPath)
        self.selectCity(city)
        
        
        thread.start_new_thread(saveActivePlayers,(elem,))
        return

    def screen(self, name):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        self.br.save_screenshot( r"C:\Users\mati\Desktop\Python" + "\\" + name + time.strftime("%Y-%m-%d_%H-%M-%S") +".png")

    def waitForVisibility(self, xPath):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        return WebDriverWait(self.br,20).until(EC.visibility_of_element_located((By.XPATH, xPath)))

    def waitForPresence(self, xPath):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        return WebDriverWait(self.br,20).until(EC.presence_of_element_located((By.XPATH, xPath)))

    def findBarbarians(self):
        t = timeWatch()
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())          
        xPath = "//*[@id='dialogContainer']/div/div[3]/div[2]/div"
        if(self.exist(xPath)):
            self.c(xPath)
            self.waitXpath(xPath, 5, False)
                
        xPath = "//*[@id='menuLinkWorldmap']/div[2]"
        self.c(xPath)
        logging.debug("After c() in " + get_function_name() + "(). Line: " + str(get_codeline() -1))
        xPath = '//*[@id="mapTile500560-204"]'
        self.waitXpath(xPath, 5, True)
        logging.debug("After waitXpath() in " + get_function_name() + "(). Line: " + str(get_codeline() -1))
        
        mapMetas = ['480540','480560','480580', 
                    '500540','500560','500580',
                    '520540','520560','520580']
        tab = []
        
        path = r'C:\Users\mati\Desktop\Python\Map.txt'
        if(os.path.exists(path) != True):
            f = open(path, 'w')
            f.flush()
            f.close()
            
        
        f = open(path, 'r')
        if(time.strftime('%Y:%m:%d') != f.readline()[:10]):
            t.start()
            for i in mapMetas:
                xPath = '//*[@id="mapMeta' + str(i) + '"]/*[contains(@class,"mapTile")]'
                if(self.exist(xPath) == True):
                    table = self.br.find_elements_by_xpath(xPath)
                    for i in table:
                        tab.append(i.get_attribute("class"))
                else:
                    for i in range(400):
                        tasks[count].append("")
            t.stop()
            toPrint = "Filled fields in: " +str(t.show())
            self.saveToShortLog(toPrint)
            print(toPrint)
            mb.sendMessage(toPrint)
            
            
            # Zapisz wszystko do pliku
            f.close()
            f = open(path, 'w')
            f.write(time.strftime('%Y:%m:%d %H:%M:%S') + " - last update" + "\n")       
            for i in tab:
                f.write(i + "\n") 
            f.flush()
            f.close()
        else:
            for i in range(3600):
                tab.append(f.readline())
            f.close()
            

          
                       
        #tab = self.br.find_elements_by_xpath('.//*[@id="mapMain"]/div/*[contains(@class,"mapTile")]')
        toPrint = str(len(tab)) + " fields filled"
        self.saveToShortLog(toPrint)
        print(toPrint)
        mb.sendMessage(toPrint)
        
        ranges = [(0,20),(20,40),(40,60)]
        barbarianXY = []
        myVillagesXY = []
        distances = []
        matrix = [[""]*60 for i in range(60)]
        #matrix1 = [[" "]*60 for i in range(60)]
        count = 0
        for h in range(9):
            a = ranges[h%3][0]
            b = ranges[h%3][1]
            c = ranges[h/3][0]
            d = ranges[h/3][1]
            for i in range(c,d):
                for j in range(a,b):
                    matrix[i][j] = tab[count]
                    count += 1
        
        for i in range(60):
            for j in range(60):
                if(str.find(str(matrix[i][j]),"23")!= -1):
                    myVillagesXY.append((j+541,i+481))
                    #matrix1[i][j] = "X"
                if(str.find(str(matrix[i][j]),"22")!= -1):
                    barbarianXY.append((j+541,i+481))
                    #matrix1[i][j] = "0"
        # print            
        '''count = 0
        s = ""
        for i in range(60):
            for j in range(60):
                count += 1
                s += "|" + matrix1[i][j]
                if(count%60 == 0):
                    s += "|" + matrix1[i][j] + "|"
                    print(s)
                    s = ""'''

        count = 0
        for i in barbarianXY:
            x1 = float(myVillagesXY[3][1])
            y1 = float(myVillagesXY[3][0])
            x2 = float(i[0])
            y2 = float(i[1])
            d = round(math.hypot(x2-x1, y2-y1),2)

            distances.append((i[0],i[1],d))
            count += 1


        distances.sort(key=lambda x:x[2])
        toPrint = "Barbarians: " + str(len(distances))
        self.saveToShortLog(toPrint)
        print(toPrint)
        mb.sendMessage(toPrint)
        
        
        
        count = 0
        for i in distances:
            
            xPath = '//*[@id="menuLinkUnitOrders"]/div[1]'
            self.c(xPath)

            xPath = '//*[@id="unitOrdersSelectionContent"]/div[1]/div[1]/div/div'
            self.waitForPresence(xPath)
            self.waitForVisibility(xPath)
            
            xPath = '//*[@id="unitOrdersTargetFieldX"]'
            self.v(xPath, i[0])
    
            xPath = '//*[@id="unitOrdersTargetFieldY"]'
            self.v(xPath, i[1])
            
            time.sleep(5)
            
            xPath = '//*[@id="unitOrdersMissionContainer"]/div[2]'
            elem = self.waitForPresence(xPath)
            if(elem.get_attribute("class") != "unitOrdersMissionButton Attack"): 
                toPrint = str(i[0]) + " " + str(i[1]) + " don't exist"
                self.saveToShortLog(toPrint)
                print(toPrint)
                mb.sendMessage(toPrint)
                continue
                
            xPath = '//*[@id="unitOrdersTargetPlayerName"]'
            elem = self.waitForVisibility(xPath)
            level = elem.text[20:21]
            
            if(level != "4"):
                continue
            if(count == 0):
                troops = [14, 13, 3]
                troopsQuantity = [5, 40, 100]
                self.sendTroops(troops,troopsQuantity,i[0],i[1],"Attack",False)
                
            if(count == 1):
                troops = [13, 12,3]
                troopsQuantity = [23, 304, 100]
                self.sendTroops(troops,troopsQuantity,i[0],i[1],"Attack",False)
            
            if(count == 2):
                troops = [8,3]
                troopsQuantity = [1000, 100]
                self.sendTroops(troops,troopsQuantity,i[0],i[1],"Attack",False)
                
            if(count == 3):
                troops = [7,2,3]
                troopsQuantity = [2000,40, 50]
                self.sendTroops(troops,troopsQuantity,i[0],i[1],"Attack",False)
                
            if(count == 4):
                troops = [7,2,3]
                troopsQuantity = [2000,40, 50]
                self.sendTroops(troops,troopsQuantity,i[0],i[1],"Attack",False)
            
            toPrint = str(count + 1) + " barbarian attacked"
            self.saveToShortLog(toPrint)
            print(toPrint)
            mb.sendMessage(toPrint)  
            count += 1
            if(count == 5): break

    def sendTroops(self, troops, quantity, destinationX, destinationY, mission, newWindow, res = [0,0,0,0]):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        if(newWindow == True):
            xPath = '//*[@id="menuLinkUnitOrders"]/div[1]'
            self.c(xPath)
            
            xPath = '//*[@id="unitOrdersSelectionContent"]/div[1]/div[1]/div/div'
            self.waitXpath(xPath, 5, True)
        self.closeTip()
        self.closeTip()
        #TODO dodać xPath obrazków wojsk
        troopsTable = { 1  : ['//*[@id="unitLegendSpy"]', '//*[@id="unitOrdersAmountSpy"]'],
                        2  : ['//*[@id="unitLegendLancer"]', '//*[@id="unitOrdersAmountLancer"]'],
                        3  : ['//*[@id="unitLegendTrader"]', '//*[@id="unitOrdersAmountTrader"]'],
                        4  : ['//*[@id="unitLegendShaman"]', '//*[@id="unitOrdersAmountShaman"]'],
                        5  : ['//*[@id="unitLegendQuipucamayoc"]', '//*[@id="unitOrdersAmountQuipucamayoc"]'],
                        6  : ['//*[@id="unitLegendPochteca"]', '//*[@id="unitOrdersAmountPochteca"]'],
                        7  : ['//*[@id="unitLegendBowman"]', '//*[@id="unitOrdersAmountBowman"]'],
                        8  : ['//*[@id="unitLegendAtlatl"]', '//*[@id="unitOrdersAmountAtlatl"]'],
                        9  : ['//*[@id="unitLegendSettler"]', '//*[@id="unitOrdersAmountSettler"]'],
                        10 : ['//*[@id="unitLegendAmazon"]', '//*[@id="unitOrdersAmountAmazon"]'],
                        11 : ['//*[@id="unitLegendNahual"]', '//*[@id="unitOrdersAmountNahual"]'],
                        12 : ['//*[@id="unitLegendEagle"]', '//*[@id="unitOrdersAmountEagle"]'],
                        13 : ['//*[@id="unitLegendJaguar"]', '//*[@id="unitOrdersAmountJaguar"]'],
                        14 : ['//*[@id="unitLegendAtlant"]', '//*[@id="unitOrdersAmountAtlant"]'],
                        15 : ['//*[@id="unitLegendEkChuah"]', '//*[@id="unitOrdersAmountEkChuah"]']}
        
        resTable = ['//*[@id="unitOrdersResLimestone"]', '//*[@id="unitOrdersResObsidian"]',
                    '//*[@id="unitOrdersResCacao"]', '//*[@id="unitOrdersResCorn"]']
                       
        missionTable ={"Spy"  : '//*[@id="unitOrdersMissionContainer"]/div[1]/div',
                       "Attack"  : '//*[@id="unitOrdersMissionContainer"]/div[2]/div',
                       "Sendres"  : '//*[@id="unitOrdersMissionContainer"]/div[4]/div',
                       "Sendtroop"  : '//*[@id="unitOrdersMissionContainer"]/div[5]'}
        if(troops[0] == "All"):
            troops = [i + 1 for i in range(15)]
            quantity = [ "All" for i in range(15)]
        troopsAvailable = []
        count = 0
        for troop in troops:
            elem = self.elem(troopsTable[troop][1]).get_attribute('outerHTML')
            if("disabled" in elem): continue
            self.waitXpath(troopsTable[troop][0],5, True)
            self.waitForVisibility(troopsTable[troop][0])
            elem = self.elem(troopsTable[troop][0])
            elem = elem.text
            elem = elem.split()
            elem = "".join(elem)
            troopsAvailable.append(elem)
            if(quantity[count] != "All"):
                if(quantity[count] > int(elem)):
                    toPrint = "Error: quantity: " + str(quantity[count]) + " is not available"
                    self.saveToShortLog(toPrint)
                    print(toPrint)
                    mb.sendMessage(toPrint)
                    xPath = '//*[@id="dialogContainer"]/div/div[3]/div[2]/div'
                    self.c(xPath)
                    xPath = '//*[@id="unitOrdersSelectionContent"]/div[1]/div[1]/div/div'
                    self.waitXpath(xPath, 10, False)
                self.v(troopsTable[troop][1],quantity[count])
            else:
                self.v(troopsTable[troop][1],"1000000")
            
            count += 1
        count = 0
        if (res[0] == "All"): res = [100000000 for i in range(4)]
        for i in resTable:
            self.v(i,res[count])
            count += 1
        
        #Ustaw koordynaty
        xPath = '//*[@id="unitOrdersTargetFieldX"]'
        self.v(xPath, destinationX)
        xPath = '//*[@id="unitOrdersTargetFieldY"]'
        self.v(xPath, destinationY)
        
        xPath = '//*[@id="unitOrdersTargetPlayerName"]'
        self.waitXpath(xPath, 5, True)
        #cel misji
        self.c(missionTable[mission])
        
        xPath = '//*[@id="glifobarTopContent"]/div[5]/div[2]/div'
        elem = self.elem(xPath)
        cornQuantity = elem.text
        cornQuantity = cornQuantity.split()
        cornQuantity = "".join(cornQuantity)
        cornQuantity = int(cornQuantity)
        
        xPath = '//*[@id="unitOrdersCostsAmount"]'
        self.waitXpath(xPath, 5, True)
        elem = self.elem(xPath)
        cornNecessary = elem.text
        cornNecessary = cornNecessary.split()
        cornNecessary = "".join(cornNecessary)
        cornNecessary = int(cornNecessary)
        
        if(cornQuantity < cornNecessary):
            toPrint = "Not enought corn to fulfil mission. Need: " + str(cornNecessary - cornQuantity) + " more"
            self.saveToShortLog(toPrint)
            print(toPrint)
            mb.sendMessage(toPrint)
        #wyslij jednostki
        xPath = '//*[@id="unitOrdersTargetSendButton"]'
        self.c(xPath)
        
        xPath = '//*[@id="unitOrdersSelectionContent"]/div[1]/div[1]/div/div'
        self.waitXpath(xPath, 10, False)

    def saveProgramData(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        path = r'C:\Users\mati\Desktop\Python\ProgramData'
        if(os.path.exists(path) != True):
            f = open(path, 'w')
            f.flush()
            f.close()
        
        f = open(path, 'wb')
        pickle.dump(self.isBarbariansAttacked, f)
        f.close()

    def loadProgramData(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        path = r'C:\Users\mati\Desktop\Python\ProgramData'
        if(os.path.exists(path) == True):
            f = open(path, 'rb')
            self.isBarbariansAttacked = pickle.load(f)

    def closeWindow(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        xPath = "//*[@id='dialogContainer']/div/div[3]/div[2]/div"
        if(self.exist(xPath)):
            self.c(xPath)
            self.waitXpath(xPath, 5, False)

    def checkIfEnemyAttack(self):
        def escape(timeToEscape):
            logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
            time.sleep(timeToEscape)
            #self.sendTroops(["All"],["All"],564,512,"Sendtroop",True,["All"])
            self.sendTroops([3],[10],564,512,"Sendtroop",True,["All"])
            time.sleep(12)
            #   Poczekaj na załadowanie treści
            xPath = '//*[@id="eventsList"]/div'
            self.waitXpath(xPath, 5, True)
            #   Przeszukaj aktywności. Jeśli atak to pobierz
            if(self.elem(xPath).text == u"(brak wydarzeń)"): return
            xPath = '//*[@id="eventsList"]/div/div[1]//*[contains(@class,"eventPanelEntry")]'
            events = self.elems(xPath)
            for i in events:
                xPath = './/*[contains(text(),"Własne wojska")]'
                if(self.elemExist(i,xPath)):
                    xPath = './/div[2]/div[3]/div[1]/table/tbody/tr[2]/td/div/*[contains(text(),"565:511")]'
                    if(self.elemExist(i,xPath)):
                        xPath = './/*[contains(@class,"tbutton primary mini2")]'
                        exit = i.find_element_by_xpath(xPath)
                        exit.click()
                        count = 0
                        while(exit.text != u"przerwać?"):
                            if(count == 10): break
                            time.sleep(0.1)
                            count += 0.1
                        exit.click()
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        try:
            #   Jeśli jest otwarte jakieś okno to je zamknij
            self.closeWindow()
            #   Otwórz okno aktywności       
            xPath = '//*[@id="menuLinkActivity"]/div[1]/div[2]'
            self.waitForVisibility(xPath)
            self.waitForPresence(xPath)
            self.c(xPath)
            ActionChains(self.br).release().perform()
            ActionChains(self.br).move_by_offset(100,100).perform()
            #   Poczekaj na załadowanie treści
            xPath = '//*[@id="eventsList"]/div'
            self.waitXpath(xPath, 5, True)
            #   Przeszukaj aktywności. Jeśli atak to pobierz
            try:
                if(self.elem(xPath).text == u"(brak wydarzeń)"): return
            except NoSuchElementException:
                logging.debug("NoSuchElementException in checkIfEnemyAttack")
                return
            xPath = '//*[@id="eventsList"]/div/div[1]//*[contains(@class,"eventPanelEntry")]'
            attacks = []
            self.waitXpath(xPath,5,True)

            events = self.elems(xPath)
            if(len(events) == 0): return
            for i in events:
                xPath = './/*[contains(text(),"Obce wojska")]'
                if(self.elemExist(i,xPath)):
                    elem = i.find_element_by_xpath(xPath)
                    for j in range(4):
                        elem = elem.find_element_by_xpath("..")
                    elem = elem.find_element_by_xpath('.//*[contains(@id,"eventProgressTime")]')
                    xPath = './div[2]/div[3]/div[2]/table/tbody/tr[2]/td/div/*[contains(text(),"565:511")]'
                    if(self.elemExist(i,xPath)):
                        attacks.append(elem.text)
            if(len(attacks) == 0):
                xPath = '/html/body/div[2]/div/div[7]/div[2]/div'
                if(self.exist(xPath)): self.c(xPath)
                else: return
            else:
                #    Zamień stringi z czasem na int
                for i in attacks:
                    hours = int(i[:2])
                    minutes = int(i[3:5])
                    seconds = int(i[6:8])
                    timeToAttack = seconds + 60 * minutes + 60 * 60 * hours
                    if(timeToAttack < 12):
                        toPrint = "It will be hurts"
                        self.saveToShortLog(toPrint)
                        print(toPrint)
                        mb.sendMessage(toPrint)
                    elif(timeToAttack > 12 and timeToAttack < 22):
                        timeToEscape = timeToAttack - 12
                        escape(timeToEscape)
                    else:
                        timeToEscape = timeToAttack - 12 - 10
                        escape(timeToEscape)
        except TimeoutException:
            logging.debug("TimeoutException in checkIfEnemyAttack.")
            return
        except StaleElementReferenceException:
            logging.debug("StaleElementReferenceException in " + get_function_name())
            return

    def elem(self, xPath):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        elem = self.br.find_element_by_xpath(xPath)
        return elem

    def elems(self, xPath):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        elems = self.br.find_elements_by_xpath(xPath)
        return elems

    def logout(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        #kliknij przycisk wylogowania
        xPath = '//*[@id="menuLogout"]'
        self.c(xPath)
        #czekaj na menu główne
        xPath = '//*[@id="startPageMainContentTabsContent"]/div[1]/div'
        self.waitXpath(xPath, 5, True)

    def sendResToMainVillage(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        resTable = ['//*[@id="glifobarTopContent"]/div[1]/div[2]/div',  #limestone
                    '//*[@id="glifobarTopContent"]/div[2]/div[2]/div',  #obsidian
                    '//*[@id="glifobarTopContent"]/div[3]/div[2]/div',  #cocoa
                    '//*[@id="glifobarTopContent"]/div[5]/div[2]/div',  #corn
                    '//*[@id="glifobarTopContent"]/div[6]/div[2]/div']  #population
        resToSend = [0,0,0]
        send = False
        for i in range(3):
            self.waitXpath(resTable[i],5,True)
            elem = self.elem(resTable[i]).text
            elem = elem.split()
            elem = "".join(elem)
            elem = int(elem)
            if( i == 0 and elem > 100000):
                if(send == False): send = True
                resToSend[i] = 100000
            if( i == 1 and elem > 50000):
                if(send == False): send = True
                resToSend[i] = 50000
            if( i == 2 and elem > 20000):
                if(send == False): send = True
                resToSend[i] = 20000
        if(send == True):
            self.sendTroops([3], [85], 565, 511, "Sendres", True, res = [resToSend[0],resToSend[1],resToSend[2],0])
            toPrint = "Res sent [" + str(resToSend[0]) + "," + str(resToSend[1]) + "," + str(resToSend[2]) + "]"
            self.saveToShortLog(toPrint)
            print(toPrint)
            mb.sendMessage(toPrint)
            send == False   

    def waitXpath(self, xPath, timeToBreak, isDifferentFrom):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        count = 0
        while(self.exist(xPath) != isDifferentFrom):
            if(count == timeToBreak): break
            time.sleep(1) 
            count += 1 

    def loginFb(self):
    	# Security hidden
        self.v(".//*[@id='email']" , "************************")
        # Security hidden
        self.v('//*[@id="pass"]' , "************************")
        self.c('//*[@id="loginbutton"]')

    def openMessages(self, name):
        def sendMessage(message):
            xPath = '//*[@placeholder = "Napisz odpowiedź…"]'
            self.waitXpath(xPath, 5, True)
            if(type(message) != type(u"")): message = message.decode("utf-8")
            self.v(xPath, message + "\n")
        def sendMenu(commandsTable):
            xPath = '//*[@placeholder = "Napisz odpowiedź…"]'
            self.waitXpath(xPath, 5, True)
            self.c(xPath)
            elem = self.elem(xPath)
            for i in commandsTable:
                if(type(i) != type(u"")): i = i.decode("utf-8")
                if(i == commandsTable[0]):
                    elem.send_keys(u"Commands:")
                    ActionChains(self.br).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).perform()
                elem.send_keys(i)
                ActionChains(self.br).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).perform()
                if(i == commandsTable[len(commandsTable)-1]):
                    ActionChains(self.br).key_up(Keys.ENTER).perform()

                
        global mb
        name = name.decode("utf-8")
        #click message button at the top
        xPath = '//*[contains(@class,"_2n_9")]' #message button
        self.waitXpath(xPath, 5, True)
        elems = self.elems(xPath)
        elems[1].click()
        #find label to open messages
        xPath = '//*[contains(text(),"Zobacz wszystkie")]'
        self.waitXpath(xPath, 5, True)
        elems = self.elems(xPath)
        elems[1].click()
        #find Szukaj form
        xPath = '//*[contains(@class,"uiSearchInput _3c")]'
        self.waitXpath(xPath, 5, True)
        elem = self.elem(xPath)
        xPath = './/*[contains(@class,"inputtext")]'
        self.waitXpath(xPath, 5, True)
        elem = self.findInElem(elem,xPath)
        elem.send_keys(name)
        
        xPath = './/*[contains(@class,"_33y img")]'
        self.waitXpath(xPath, 10, False)
        
        def findPerson():
            xPath = '//*[contains(@class,"accessible_elem") and contains(text(),"' + name + '")]'
            self.waitXpath(xPath, 5, True)
            elems = self.elems(xPath)
            try:
                elem = elems[1].find_element_by_xpath("..")
            except NoSuchElementException:
                findPerson()
            except IndexError:
                findPerson()
        findPerson()

        elem.click()
        print("Fb Ready")
        #download messages
        xPath = '//*[contains(@class,"_38 direction_ltr")]'
        self.waitXpath(xPath, 5, True)
        elems = self.elems(xPath)
        lastMessages = elems
        commands =["kod 007" , "ping" , "show me", "exit"]
        isTentlanStopped = False
        while(True):
            try:
                if(Bot.isKeyboardInterrupt == True): raise KeyboardInterrupt
                xPath = '//*[contains(@class,"_38 direction_ltr")]'
                self.waitXpath(xPath, 5, True)
                elems = self.elems(xPath)
                currentMessages = elems
                if(isTentlanStopped != True):
                    if(mb.isCommunication == True):
                        if(mb.isMessageToSend == True):
                            mb.isMessageToSend = False
                            sendMessage(mb.messageToSend)
                            mb.isMessageReceived = True
                if(len(lastMessages) != len(currentMessages)):
                    if(len(currentMessages) == 0): continue
                    elem = currentMessages[len(currentMessages)-1]
                    try:
                        message = self.findInElem(elem, "./*").text
                    except StaleElementReferenceException:
                        continue
                    if(message == "kod 007"): sendMessage("007 zgłaszam się")
                    if(message == "ping"): sendMessage("pong")
                    if(message == "stop"):
                        sendMessage("Tentlan stopped")
                        isTentlanStopped = True
                    if(message == "start"):
                        sendMessage("Tentlan start")
                        isTentlanStopped = False
                    if(message == "help"): sendMenu(commands)
                    if(message.lower() == "show me"):
                        mb.isCommunication = True
                        sendMessage("Communication is on")
                    if(message.lower() == "exit"):
                        mb.isCommunication = False
                        sendMessage("Communication is off")
                    lastMessages = currentMessages
                time.sleep(0.1)
            except TimeoutException:
                toPrint = "TimeoutException in " + get_function_name()
                print(toPrint)
                self.saveToShortLog(toPrint)
                continue
            
    def findInElem(self, elem, xPath):
        elem = elem.find_element_by_xpath(xPath)
        return elem

    def findInElems(self, elem, xPath):
        elem = elem.find_elements_by_xpath(xPath)
        return elem

    def saveToShortLog(self, toWrite):
        path = r'C:\Users\mati\Desktop\Python\Output.txt'
        if(os.path.exists(path) != True):
            f = open(path, 'w')
            f.flush()
            f.close()
        if(type(toWrite) == type(u"")): toWrite = toWrite.encode("utf-8")
        else: toWrite = str(toWrite)
        f = open(path, "a")
        f.write(toWrite + "\n")
        f.flush()
        f.close()

    def logoutFb(self):
        xPath = '//*[@class="_5lxt f_click"]'
        self.waitXpath(xPath, 10, True)
        self.c(xPath)
        
        xPath = '//*[contains(text(),"Wyloguj się")]//*[@class="_54nh"]'

    def closeTip(self):
        xPath = '//*[@id="statusContainer"]/div/a'
        if(self.exist(xPath)): self.c(xPath)
        self.waitXpath(xPath, 10, False)
        
class timeWatch:
    t1 = 0
    t2 = 0

    def start(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        timeWatch.t1 = time.time()

    def stop(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        timeWatch.t2 = time.time()

    def show(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        time = str(round(timeWatch.t2-timeWatch.t1,2))
        return time  

class PlayersOnline:

    players = []
    currentFlag = 0
    previousFlag = 0
    t = None
    
    def whoIsOnline(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        self.update()
        while(True):
            self.currentFlag = str.find(self.t, '"flagInactive":false', self.previousFlag + 1)
            if(self.currentFlag == -1):
                f = open(r"C:\Users\mati\Desktop\Python\test.txt", "w")
                f.write(str(self.players))
                f.flush
                f.close()
                temp = []
                for e in set(self.players):
                    temp.append(e)
                self.players = temp
                break
            firstCharacterUsername = str.rfind(self.t, '"username":"', self.previousFlag, self.currentFlag) + len('"username":"')
            lastCharacterUsername = str.find(self.t, '"', firstCharacterUsername)
            self.players.append(self.t[firstCharacterUsername : lastCharacterUsername])
            self.previousFlag = self.currentFlag
        return self.players

    def update(self):
        logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
        f = open(r"C:\Users\mati\Desktop\Python\tekst.txt")
        self.t = f.read()
        f.close()  

class MessageBride:

    isCommunication = False
    isMessageToSend = False
    isMessageReceived = False
    messageToSend = ""

    def sendMessage(self, message):
        global mb
        if(mb.isCommunication == True):
            mb.messageToSend = message
            mb.isMessageToSend = True
            while(True):
                if(mb.isMessageReceived == True):
                    mb.isMessageReceived = False
                    break
                time.sleep(0.1)

def tentlanLoop(b):
    logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
    try:

        #t1 = Thread(target=closeProgram,args=("16:45:00",))
        #t1.start()
        global mb
        refresh = False
        tentlanLoop.isKeyboardInterrupt = False
        b.isKeyboardInterrupt = False
        global isQuit
        b.br.get('http://pl2.tentlan.com')

        b.checkIfResponding(b.isLogged)

        t = timeWatch()
        t.start()   
        b.login()

        while(b.isTaskStopped):
            b.isTaskStopped == False
            b.login()
        t.stop()
        print("Logged to tentlan in: " + t.show())
        xPath = "//*[@id='citymapContent']/map/area[1]"
        b.waitForVisibility(xPath)
        b.waitForPresence(xPath)
        #b.screen("AfterLogin")
        ad = "//*[@id='dialogContainer']/div/div[3]/div[2]/div"
        
        if(b.exist(ad)):
            b.c(ad)
        xPath = "//*[@id='citySelector']/div[1]/div[3]"
        b.waitForPresence(xPath)
        b.waitForVisibility(xPath)

        xPath = '//*[@id="citymapContent"]/map/area[1]'
        b.waitXpath(xPath, 10, True)
        b.waitForPresence(xPath)
        b.waitForVisibility(xPath)
        #b.screen("AfterAdvert")
        #'//*[@id="dialogContainer"]/div/div[3]/div[2]/div'

        #dobre miejsce na testy
        

        cities = ["city1", "city2", "city3", "city4", "city5"]
        materials = ["corn", "limestone", "obsidian", "cocoa"]
        count = 0

        while(True):
            for city in cities:
                t.start()
                b.selectCity(city)
                b.checkIfEnemyAttack()
        
                for material in materials:
                    b.collect(material, city)
                    if(material == "obsidian"): b.move(city)

                if(city != "city1"): b.sendResToMainVillage()

                t.stop()   
                count += 0.2
                var = str(count)
                toPrint = time.strftime("%H:%M:%S ") + var + " " + t.show()
                b.saveToShortLog(toPrint)
                print(toPrint)
                mb.sendMessage(toPrint)
                

    except TimeoutException:
        logging.debug("TimeoutException in " + get_function_name())
        b.screen("TimeoutException")
        toPrint = "Timeout Exception in " + get_function_name()
        b.saveToShortLog(toPrint)
        print(toPrint)
        mb.sendMessage(toPrint)
        refresh = True
        isQuit = True
    except KeyboardInterrupt:
        tentlanLoop.isKeyboardInterrupt = True
        b.isKeyboardInterrupt = True
        logging.debug("KeyboardInterrupt in " + get_function_name())
    except WebDriverException:
        logging.debug("WebDriverException in " + get_function_name())
    except StaleElementReferenceException:
        logging.debug("StaleElementReferenceException in " + get_function_name())
    finally:
        #if(refresh == True): tentlanLoop()
        logging.debug("Finally " + get_function_name())
        isQuit = True
        Bot.quitCountDown = True
        if(tentlanLoop.isKeyboardInterrupt == True):
            isQuit = False
        else:
            def logoutloop():
                try:
                    b.logout()
                except TimeoutException:
                    toPrint = ("TimeoutException in " + get_function_name())
                    print(toPrint)
                    b.saveToShortLog(toPrint)
                    logoutloop()
            logoutloop()
            
                
        toPrint ="Finally block in " + get_function_name()
        bot.saveToShortLog(toPrint)
        print(toPrint)
        mb.sendMessage(toPrint)
        b.saveProgramData()

def fbLoop(b):
    logging.debug("Thread: " + threading.current_thread().getName() + ". In " + get_function_name() + get_function_parameters_and_values())
    def fbLoopInLoop():
        pass
        
    try:
        global fbClosed
        isClosed = False
        inFinally = False
        b.br.get("https://www.facebook.com")
        t = timeWatch()
        if(inFinally != True):
            t.start()
            b.loginFb()
            t.stop()
            print("Logged to facebook in: " + t.show())
        else:
            print("Refresh fb")
    	# Security hiddden
        b.openMessages("*** Mateusz ***** Krogul ***")
    except KeyboardInterrupt:
        logging.debug("KeyboardInterrupt in " + get_function_name())
    finally:
        if(Bot.isKeyboardInterrupt != True):
            inFinally = True
            fbLoop(b)
        fbClosed == True
        if(isClosed == False):
            b.br.quit()
            isClosed = True
        
logging.basicConfig(filename=r'C:\Users\mati\Desktop\Python\test.log',level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')   
LOGGER.setLevel(logging.WARNING)
logging.info('"test.py" started')
try:
    mb = MessageBride()
    bot = Bot()
    bot.test(False)
    isQuit = True
    #fb = Bot()
    fbClosed = False
    #fb.test(False)
    count = 1
    while(True):
        logging.info("tentlanLoop run. " + str(count) + " iteration.")
        if(isQuit == True):
            isQuit = False
            if(count == 1):
                #t1 = Thread(target=fbLoop, args=(fb,))
                #t1.start()
                pass
            tentlanLoop(bot)
            count += 1
        if(tentlanLoop.isKeyboardInterrupt == True): break
    Bot.isKeyboardInterrupt = True
    
finally:
    logging.info('"test.py" finished')
    bot.br.quit()
    if(fbClosed == True): print ("OK")


    


          

    
