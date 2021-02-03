import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('192.168.1.15')
x = 77
y = 12
z = -3
mc.setBlock(x,y,z,block.IRON_BLOCK)
mc.setBlock(x,y+1,z,block.IRON_BLOCK)
mc.setBlock(x,y+2,z,block.IRON_BLOCK)
mc.setBlock(x+1,y+2,z,block.IRON_BLOCK)
mc.setBlock(x-1,y+2,z,block.IRON_BLOCK)
mc.setBlock(x,y+3,z,block.LIT_PUMPKIN)
