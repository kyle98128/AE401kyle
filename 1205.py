from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def buildPyramid(x,y,z,base):

    height = (base//2) + 1
    
    
    
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        
        x2 = x + base - i
        z2 = z + base - i
        
        
        mc.setBlocks(x1, y1, z1, x2, y, z2, 57)
        
x,y,z = mc.player.getTilePos()
base = int(input('enter base:'))   
buildPyramid(x, y, z, base)        