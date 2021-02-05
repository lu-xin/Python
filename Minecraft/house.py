import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create("192.168.1.15", 4711)
#pos = mc.entity.getTilePos(1927)
#print (pos.x,pos.y,pos.z)
mc.postToChat("welcome to Lucie's world!")
x = 77
y = 12
z = -3
print(x, y, z)
mc.setBlocks(x - 5, y, z + 5, x + 5, y + 5, z + 6, block.DIAMOND_BLOCK)
mc.setBlocks(x - 5, y, z - 6, x + 5, y + 5, z - 5, block.DIAMOND_BLOCK)
mc.setBlocks(x + 5, y, z - 6, x + 6, y + 5, z + 6, block.DIAMOND_BLOCK)
mc.setBlocks(x - 6, y, z - 6, x - 5, y + 5, z + 5, block.DIAMOND_BLOCK)
mc.setBlocks(x - 6, y + 6, z - 6, x + 6, y + 6, z + 6, block.DIAMOND_BLOCK)
mc.setBlocks(x, y + 6, z, x, y + 6, z, block.TORCH)
