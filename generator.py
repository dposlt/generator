#!/usr/bin/env python3

__author__ = 'David Poslt'

import pyautogui
from ascii import ASCII

largeChart = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

position = []

def mousePosition():
    count = 16
    print('Move mouse to quit.')

    while len(position) != count:
        x, y = pyautogui.position()
        positionX = str(x).rjust(4)
        positionY = str(y).rjust(4)

        if int(positionX) > 126 or int(positionY) > 126:
            positionX = int(positionX[:-1])
            positionY = int(positionY[:-1])


            if positionX in ASCII.showASCITable() and positionY in ASCII.showASCITable():
                position.append(ASCII.showASCITable()[positionX])

                position.append(ASCII.showASCITable()[positionY])



mousePosition()
print(position)