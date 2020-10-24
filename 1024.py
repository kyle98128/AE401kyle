mc.setBlocks(x,y,z,x,y,z,20)


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time 

while True:
    
    x,y,z = mc.player.getTilePos()
     
    a = mc.getBlock(x+1, y-1, z)
    b = mc.getBlock(x-1, y-1, z)
    c = mc.getBlock(x, y-1, z+1)
    d = mc.getBlock(x, y-1, z-1)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
       
        mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 20)
    
while True:    
        x,y,z = mc.player.getTilePos()
        mc.setBlock(x, y, z, 38)
        time.sleep(0.2)            
        
x,y,z = mc.player.getTilePos()
a = 0
while a < 8:
    mc.setBlocks(x+20, y-1, z, x-20, y-10, z, 19)
    z = z + 5
    a = a + 1  

while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(5)    