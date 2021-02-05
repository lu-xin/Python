import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
a = mc.player.getEntities(20)
for x in a:
    print(x[0],x[2])
