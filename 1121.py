from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x,y,z = mc.player.getTilePos()


for i in range(20):
    mc.setBlocks(x+i,y,z+i,x+i,y,z+i+2,1)


    
x,y,z = mc.player.getTilePos()    
mc.setBlocks(x,y,z, x,y+2,z,1)
mc.setBlocks(x-1,y+3,z-1, x+1,y+5,z+1,57)
