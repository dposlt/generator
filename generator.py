#!/usr/bin/env python3

__author__ = 'David Poslt'

import random
import pyautogui

charts = 'abcdefghijklmnopqrstuvwxyz1234567890#@!'
count = 12
position = []

while count != 0:
    mouse = pyautogui.position()
    x = mouse[0]
    y = mouse[1]
    position.append(x)
    position.append(y)
    count -=1


print(position)
retezec = random.sample(charts,12)

print(''.join(retezec))
