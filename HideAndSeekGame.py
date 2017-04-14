# Original creator: Martin O'Hanlon (https://github.com/martinohanlon/minecraft-hs)

# This game places a diamond block within 50 random blocks from your current location.
# Your mission is to find it by following the "hot" and "cold"-style hints as you move,
# and since you are being timed, try to do so as fast as you can.


from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
import mcpi.block as block


import time
import random
import math

#function to round players float position to integer position
def roundVec3(vec3):
    return Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

def distanceBetweenPoints(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))
    
if __name__ == "__main__":

    mc = Minecraft.create()
    pos = mc.player.getPos()


    #Post a message to the minecraft chat window 
    mc.postToChat("Hi, Minecraft Hide & Seek")

    time.sleep(2)
    
    #Find the players position
    playerPos = mc.player.getPos()
    
    #Create random position within 50 blocks from the player, our hidden block will go there
    randomBlockPos = roundVec3(playerPos)
    randomBlockPos.x = random.randrange(randomBlockPos.x - 50, randomBlockPos.x + 50)
    randomBlockPos.y = random.randrange(randomBlockPos.y - 5, randomBlockPos.y + 5)
    randomBlockPos.z = random.randrange(randomBlockPos.z - 50, randomBlockPos.z + 50)
    print(randomBlockPos)
    
    #Create hidden diamond block
    mc.setBlock(randomBlockPos.x, randomBlockPos.y, randomBlockPos.z, block.DIAMOND_BLOCK)
    mc.postToChat("A diamond has been hidden - go find!")
    
    #Start hide and seek
    seeking = True
    lastPlayerPos = playerPos
    lastDistanceFromBlock = distanceBetweenPoints(randomBlockPos, lastPlayerPos)
    timeStarted = time.time()
    while (seeking == True):
        #Get players position
        playerPos = mc.player.getPos()
        #Has the player moved
        if lastPlayerPos != playerPos:
            #print "lastDistanceFromBlock = " + str(lastDistanceFromBlock)
            distanceFromBlock = distanceBetweenPoints(randomBlockPos, playerPos)
            #print "distanceFromBlock = " + str(distanceFromBlock)
            if distanceFromBlock < 2:
                #found it!
                seeking = False
            else:
                if distanceFromBlock < lastDistanceFromBlock:
                    mc.postToChat("Warmer " + str(int(distanceFromBlock)) + " blocks away")
                if distanceFromBlock > lastDistanceFromBlock:
                    mc.postToChat("Colder " + str(int(distanceFromBlock)) + " blocks away")
            
            lastDistanceFromBlock = distanceFromBlock
            
        time.sleep(2)
    timeTaken = time.time() - timeStarted
    mc.postToChat("Well done - " + str(int(timeTaken)) + " seconds to find the diamond")

    time.sleep(5)
