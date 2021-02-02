import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('192.168.1.15')
allIds = mc.getPlayerEntityIds()
print(allIds)
