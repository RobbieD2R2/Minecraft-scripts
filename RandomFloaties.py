# Randomly place different blocks in the air surroundingthe player's current position


from mcpi.minecraft import Minecraft
from random import randint

mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z



# 100 Floating colored wool blocks

for i in range(0,100):
    myBlockData = randint(1,15)
    myX = randint(-50,50)
    myZ = randint(-50,50)

    mc.setBlock(x+myX, y+5, z+myZ, 35, myBlockData)




# 100 Floating flowers (they will soon fall to the ground)

#for i in range(0,100):
#    myBlockData = randint(1,8)
#    myX = randint(-50,50)
#    myZ = randint(-50,50)

#    mc.setBlock(x+myX, y+5, z+myZ, 38, myBlockData)
