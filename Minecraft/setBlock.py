import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
#x,y,z=77,12,-3
x,y,z=-144,6,-119
mc.setBlock(x,y,z,block.DOOR_BIRCH)
mc.setBlock(x,y+1,z,block.DOOR_BIRCH)
