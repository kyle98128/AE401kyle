# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:18:23 2020

@author: changyunchen
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()




while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits [0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        if block == 0:
            mc.setBlock(x,y,z, 57)
x,y,z, = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'黑黑黑愛滋味麥仔茶(要用台語說)','','','')

from mcpi.minecraft import Minecraft
import random
import time


mc = Minecraft.create()
i = 0
while i < 20: 
    pos = mc.player.getPos()
    i = i+1
    x = pos.x + random.uniform(-20,20)
    y = pos.y + random.uniform(3,0)
    z = pos.z + random.uniform(-20,20)
    
    
    mc.spawnEntity(x,y,z,12)
    time.sleep(0.5)