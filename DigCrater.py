# Dig a crater (hole) 5 blocks deep


from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()
pos = mc.player.getPos()

print("Your position is: ", pos.x, pos.y, pos.z)

x = pos.x
y = pos.y
z = pos.z+5

mc.setBlocks(x, y, z, x+10, y-5, z+10, 0)

mc.postToChat("We just dug a crater!")

