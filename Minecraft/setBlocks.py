import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('192.168.1.15')
x,y,z=77,12,-3
mc.setBlocks(x-10,y,z-10,x+10,y,z+10,block.AIR)
