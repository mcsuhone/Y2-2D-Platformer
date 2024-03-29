from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.Qt import QPixmap


class Block(QGraphicsPixmapItem):
    
    def __init__(self, x, y, scene, texture = "Textures/Blocks/BlockGrass.png", collision = True, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap(texture))
        self.addPos(x,y)
        self.collision = collision
        scene.addItem(self)
        
    def X0(self):
        
        return self.x()
    
    def Y0(self):
        
        return self.y()
        
    def right_side(self):
        
        return 0
        
    def addPos(self,x,y):
        self.setPos(x*32,y*32)
        
    def is_collidable(self):
        if self is None:
            return False
        else:
            return self.collision
        
    def stand_on_effect(self,player,scene):
        
        return False
        
    def touch_effect(self,player,scene):
        
        pass