#!/etc/bin/env python

__author__ = 'David Poslt'

import random

charts = 'abcdefghijklmnopqrstuvwxyz1234567890#@!'
delka = 0
retezec = []

while delka <=11:
    delka +=1
    retezec.append(random.choice(charts))


print(*retezec)
