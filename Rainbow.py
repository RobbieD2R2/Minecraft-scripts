# Create a rainbow


from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z+5

i=0
a=0   #increments the x-coordinate
b=0   #increments the y-coordinate
while i<10:
        mc.setBlock(x+a, y+b, z, 95, 10)
        mc.setBlock(x+a, y+b+1, z, 95, 11)
        mc.setBlock(x+a, y+b+2, z, 95, 3)
        mc.setBlock(x+a, y+b+3, z, 95, 13)
        mc.setBlock(x+a, y+b+4, z, 95, 4)
        mc.setBlock(x+a, y+b+5, z, 95, 1)
        mc.setBlock(x+a, y+b+6, z, 95, 14)
        a+=1
        mc.setBlock(x+a, y+b, z, 95, 10)
        mc.setBlock(x+a, y+b+1, z, 95, 11)
        mc.setBlock(x+a, y+b+2, z, 95, 3)
        mc.setBlock(x+a, y+b+3, z, 95, 13)
        mc.setBlock(x+a, y+b+4, z, 95, 4)
        mc.setBlock(x+a, y+b+5, z, 95, 1)
        mc.setBlock(x+a, y+b+6, z, 95, 14)
        a+=1
        b+=1
        i+=1
mc.setBlocks(x+a, y+b, z, x+a+6, y+b, z, 95, 10)
mc.setBlocks(x+a, y+b+1, z, x+a+6, y+b+1, z, 95, 11)
mc.setBlocks(x+a, y+b+2, z, x+a+6, y+b+2, z, 95, 3)
mc.setBlocks(x+a, y+b+3, z, x+a+6, y+b+3, z, 95, 13)
mc.setBlocks(x+a, y+b+4, z, x+a+6, y+b+4, z, 95, 4)
mc.setBlocks(x+a, y+b+5, z, x+a+6, y+b+5, z, 95, 1)
mc.setBlocks(x+a, y+b+6, z, x+a+6, y+b+6, z, 95, 14)
j=0
a=26
b=10
while j<11:
        mc.setBlock(x+a, y+b, z, 95, 10)
        mc.setBlock(x+a, y+b+1, z, 95, 11)
        mc.setBlock(x+a, y+b+2, z, 95, 3)
        mc.setBlock(x+a, y+b+3, z, 95, 13)
        mc.setBlock(x+a, y+b+4, z, 95, 4)
        mc.setBlock(x+a, y+b+5, z, 95, 1)
        mc.setBlock(x+a, y+b+6, z, 95, 14)
        a+=1
        mc.setBlock(x+a, y+b, z, 95, 10)
        mc.setBlock(x+a, y+b+1, z, 95, 11)
        mc.setBlock(x+a, y+b+2, z, 95, 3)
        mc.setBlock(x+a, y+b+3, z, 95, 13)
        mc.setBlock(x+a, y+b+4, z, 95, 4)
        mc.setBlock(x+a, y+b+5, z, 95, 1)
        mc.setBlock(x+a, y+b+6, z, 95, 14)
        a+=1
        b-=1
        j+=1
