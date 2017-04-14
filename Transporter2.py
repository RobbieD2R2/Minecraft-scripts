# Once the player enters the Teleporter Device they are
# immediately relocated to the closest NetherPortal
# NOTE: these XYZ coordinates are unique to my MC server world


from mcpi.minecraft import Minecraft
import time


def teleport():
    
    mc.postToChat("BINGO!")
    mc.player.setPos(-453, 4, -255)


if __name__ == "__main__":
    mc = Minecraft.create()
    
    while True:
        pos = mc.player.getPos()
        x = pos.x
        y = pos.y
        z = pos.z
        
        if x<-426 and x>-427 and y==4 and z<-199 and z>-200:
            teleport()
