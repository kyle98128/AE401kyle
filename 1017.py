# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:19:08 2020

@author: changyunchen
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,20)
mc.setBlock(x,y+1,z,20)
mc.setBlock(x,y+2,z,20)
mc.setBlock(x,y+3,z,20)
mc.setBlock(x,y+4,z,20)
mc.setBlock(x,y+5,z,20)
mc.setBlock(x,y+5,z,20)



x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z+1,20)e
mc.setBlock(x+1,y,z,20)
mc.setBlock(x+1,y,z+1,20)
mc.setBlock(x+1,y,z-1,20)
mc.setBlock(x-1,y,z+1,20)
mc.setBlock(x-1,y,z,20)
mc.setBlock(x-1,y,z-1,20)
mc.setBlock(x,y,z-1,20)
x,y,z = mc.player.getTilePos()
mc.setBlocks(x+50,y,z+50,x-1,y-50,z-1,100)
