from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

# Portal frame (made with Obsidian)
mc.setBlocks(x, y, z+5, x+4, y+5, z+5, 49)
mc.setBlocks(x+1, y+1, z+5, x+3, y+4, z+5, 0)

# Instruction to activate the portal
mc.postToChat("To activate the portal, use the Flint and Steel tool!")
