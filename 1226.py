
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import choice


mineral = [[14,15,16],[56,73,129]]

r = choice(mineral)

myID = mc.getPlayerEntityId('KYLETWN')
x,y,z = mc.entity.getTilePos(myID)
mc.setBlock(x,y,z,r)

list2d = [[12,41,14],[35,73,86]]
x,y,z = mc.player.getTilePos()
startX = x

for list1d in list2d:
    
    for i in list1d:
        mc.setBlock(x,y,z,i)
        
        
        x = x + 1
        
    x=startX 
    z = z+1

x,y,z = mc.player.getTilePos()   
try:
    blockType = int(input('block ID:'))
    mc.setBlock(x,y,z,blockType)
    
except:
    print('yrbegtgthhtrnyt')
    
    
    
    
while True:
    chat = mc.events.pollChatPosts()
    if len(chat) > 0:
        strChat = str(chat[0])
        length = len(strChat)
        
        comma1 = strChat.find(',',0)
        comma2 = strChat.find(',',comma1 + 1)
        
        senderID = int(strChat[comma1 + 1:comma2])
        message = strChat[comma2 +1 +1:length - 1]
        
        playerName = mc.entity.getName(senderID)
        x,y,z = mc.entity.getTilePos(senderID)
        
        mc.setSign(x,y,z,63,0,playerName,'',message)
        
        
        
    
