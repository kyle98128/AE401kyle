from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randint(1,4)
    color = random.randrange(0,16)
    
    if r ==1:
        mc.setBlocks(x,y,z,x+4,y,z,35,color) 
        x = x+4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,35,color)
        x = x-4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+3,35,color)
        z = z+4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,35,color)
        z = z-4     
    
   

    
        
    
    
    
    
    


     
    