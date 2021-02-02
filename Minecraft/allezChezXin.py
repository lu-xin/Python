import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('192.168.1.15')
allIds = mc.getPlayerEntityIds()
x,y,z=77,12,-3
for i in allIds:
    mc.entity.setPos(i, x, y, z)
    z=z+1
