from PyQt5.QtGui import QPixmap
from block import Block

class BlockGround(Block):
    
    def __init__(self,x,y, parent=None):
        Block.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\BlockGround.png"))
        self.addPos(x,y)