import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
while True:
    for chatPost in mc.player.pollChatPosts():
        with open("C:\\Minecraft\\myBlocks.txt") as f:
            lines = f.readlines()
            myChat = chatPost.message.upper()
            print(myChat[0:19])
            if myChat[0:19] == 'BABA PLEASE GIVE ME':
                myBlock = myChat[20:-1]
                print(myBlock)
                for line in lines:
                    if myBlock == line.strip():
                        x, y, z = mc.player.getTilePos()
                        a = str('mc.setBlock(%s,%s,%s,block.%s' % (x,y,z,myBlock)+')')
                        def exec_code(a):
                            exec(a)
                        exec_code(a)
