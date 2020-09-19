# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:29:46 2020

@author: changyunchen
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


mc.postToChat("i'm watching you")


while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("x:"+ str(x) + "y:" + str(y) + " Z:" + str(z))
    
