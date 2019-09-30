#!/usr/bin/env python3

__author__ = 'David Poslt'

import random
import pyautogui

charts = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

position = []

def mousePosition():
    import sys
    count = 16

    print('Move mouse to quit.')

    while len(position) != count:
        x, y = pyautogui.position()
        positionX = str(x).rjust(4)
        positionY = str(y).rjust(4)
        if positionX not in position and positionY not in position:
            position.append(positionX)
            position.append(positionY)
            #print(position)



    return position

MyPass = []
def convertToChar(number):
    for i in number:
        #i = i.strip()

        if int(i) > 33 and int(i) < 126:
            #i = i[:-1]
            i = int(i)
            MyPass.append(chr(i))
        elif int(i) !=32 :
            i = int(i)
            MyPass.append(chr(i))




convertToChar(mousePosition())

print(*MyPass)