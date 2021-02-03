import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('192.168.1.15')
#Get Players' IDs
allIds = mc.getPlayerEntityIds()
#Xin's Home
x,y,z=77,12,-3

mc.entity.setPos(allIds[1], x, y, z)
