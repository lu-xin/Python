import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('192.168.1.15')
x, y, z = mc.player.getTilePos()
print(x,y,z)
x, y, z = mc.entity.getTilePos(18767)
print(x,y,z)
