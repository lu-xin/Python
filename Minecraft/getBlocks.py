import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
with open("C:\\Minecraft\\myBlocks.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
