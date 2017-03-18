from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z
blockType = 57

mc.setBlocks(x, y+15, z, x, y+20, z, blockType)
mc.setBlocks(x, y+20, z, x+5, y+20, z, blockType)
mc.setBlocks(x+5, y+20, z, x+5, y, z, 10)
mc.setBlocks(x, y, z+5, x+10, y, z+5, blockType)
mc.setBlocks(x, y, z-5, x+10, y, z-5, blockType)
mc.setBlocks(x, y, z+5, x, y, z-5, blockType)
mc.setBlocks(x+10, y, z+5, x+10, y, z-5, blockType)
