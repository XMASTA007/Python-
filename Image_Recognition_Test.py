from pyautogui import *
import pyautogui
import keyboard
import time
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('Meep.png',  grayscale=True,  confidence = 0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
