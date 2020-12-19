# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:01:26 2020

@author: changyunchen
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange
from time import time


for i in range(10):
    x,y,z = mc.player.getTilePos()
    x = x + i
    
    
    for j in range(10):
        r = randrange(0,16)
        z = z + 1
while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        
        if data == r:
            mc.postToChat('find it')
            mc.setBlock(hit.pos,57)
            break
        elif data < r:
            mc.postToChat('bigger data')
        elif data > r:
            mc.postToChat('smaller data')
             3
            
def LinearSearch():
    sTime = time()
    r = randrange(0,100000)
    print(r)
    for i in range(100000):
        if r == i:
            print('find it' +str(i))
            print('LinearSearch' +str(time() - sTime))
            break
        
LinearSearch()