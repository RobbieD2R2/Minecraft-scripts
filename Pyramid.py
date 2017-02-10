# Creates a pyramid
# Set how large you want it with numLayers and j variables

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x+5
y = pos.y
z = pos.z+5

#Always set numLayers and j equal to the same value
numLayers=30
i=0
j=30
while i<(numLayers/2):
	mc.setBlocks(x+i, y+i, z+i, x+j, y+i, z+j, 15)
	i+=1
	j-=1
