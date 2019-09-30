#!/usr/bin/env python3

__author__ = 'David Poslt'

import random
import pyautogui

charts = 'abcdefghijklmnopqrstuvwxyz1234567890#@!'


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
mousePosition()

print(position)