from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

# Gold background
mc.setBlocks(x, y, z+5, x+20, y+20, z+5, 41)

# Eyes
mc.setBlocks(x+4, y+13, z+5, x+8, y+17, z+5, 133)
mc.setBlocks(x+13, y+13, z+5, x+17, y+17, z+5, 133)

# Smile
mc.setBlocks(x+4, y+5, z+5, x+17, y+7, z+5, 133)
mc.setBlocks(x+4, y+7, z+5, x+6, y+10, z+5, 133)
mc.setBlocks(x+15, y+7, z+5, x+17, y+10, z+5, 133)
