#!/usr/bin/env python

__author__= 'David Poslt'

class ASCII:


    def showASCITable():
        character = {}
        for num in range(33,127):
            charts = chr(num)
            character[num] = charts
            #print('{} : {}'.format(num, charts))
        return character



getChar = ASCII.showASCITable()

'''
znak = 88
if znak in getChar:
    print(getChar[znak])
'''