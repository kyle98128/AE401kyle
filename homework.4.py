from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:    
    x,y,z = mc.player.getTilePos()
    block = mc.getBlock(x, y-1, z)
    if block == 2:
       time.sleep(0.2)

    