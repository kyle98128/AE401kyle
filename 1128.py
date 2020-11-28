from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y++5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17)
    
    
    
    
    
x,y,z = mc.player.getTilePos()
plantTree(x,y,z)