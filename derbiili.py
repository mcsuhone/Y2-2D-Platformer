from PyQt5.QtGui import QPixmap,QPainterPath
from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt

from physics import Physics
from PyQt5.Qt import QTransform, QPointF

class Derbiili(QGraphicsPixmapItem):
    
    def __init__(self, scene, x, y, parent=None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("Textures\Derbiili.png"))
        
        self.collision = False
        self.setPos(x*32,y*32)
        
        self.speed = 4
        self.jump_height = 8.0
        self.jump = False
        self.vy = 0.0
        self.counter = 0
        #Height = 22
        #Widght = 26
        
        self.scene = scene
        self.physics = Physics()
        
    def is_collidable(self):
        return self.collision
    
    def player_movement(self, keys_pressed):
        
        #(self.x()-32.0),(self.y()-38.0),(self.x()+64.0),(self.y()+54.0)
        dx = 0
        
        #position = self.physics.check_collision_direction(self,nearbyitems)
        
        if Qt.Key_Space in keys_pressed:
            
            self.jump = True
        
        if self.jump:
            self.counter += 1
        if self.counter >= 3:
            self.jump = False    
        
            
        if self.physics.check_collision(self) and self.jump:
            
            self.vy = self.jump_height
            dy = self.vy
            
        elif self.physics.check_collision(self):
            
            self.counter = 0
            self.jump = False
            dy = 0
            
            self.physics.reset_gravity()
            
        else:
            self.vy = self.physics.gravity(self.vy)
            if self.vy >= 8:
                dy = 8
            else:
                dy = self.vy
        
        #if not self.physics.check_collision(self):
        if Qt.Key_A in keys_pressed:
            dx -= self.speed
        
        #if not self.physics.check_collision(self):
        if Qt.Key_D in keys_pressed:
            dx += self.speed
        
        pos = self.pos()
        pos += QPointF(0.0,31.0)
        
        '''
        itemunder = self.scene.itemAt(pos)
        
        if itemunder.y() < self.y()-dy:
            dy = itemunder.y()-self.y()
        '''
        self.setPos(self.x()+dx, self.y()-dy)
    
    def is_flying(self):
        
        if self.physics.check_collision(self):
            return False
        else:
            return True
     
        
        
        