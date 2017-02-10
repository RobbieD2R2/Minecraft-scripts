# Creates a spire (column) 25 blocks tall
# Helpful as a marker for finding your way back to shelter

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x+5
y = pos.y+5
z = pos.z+5

print("Your position is: ", x, y, z)

for i in range(5,30):
    mc.setBlock(x, y+i, z, 12)
    
