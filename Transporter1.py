# Build the Transporter Machine


from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x, y, z+5, x+5, y+5, z+8, 57)
mc.setBlocks(x+1, y, z+6, x+4, y+4, z+7, 0)
mc.setBlocks(x+3, y, z+5, x+3, y+3, z+5, 0)
mc.setBlocks(x+1, y, z+6, x+4, y, z+7, 171)
