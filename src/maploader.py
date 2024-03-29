from io import StringIO

from Blocks.spikes import Spikes
from derbiili import Derbiili
from Items.cake import Cake
from Blocks.portal import Portal
from Creatures.snake import Snake
from Creatures.bat import Bat
from Blocks.blockice import BlockIce
from Creatures.cavebug import CaveBug
from Creatures.ghost import Ghost
from Blocks.checkpoint import Checkpoint
from Items.flower import Flower
from Items.crown import Crown
from Blocks.lava import Lava
from Creatures.platform import Platform
from Blocks.block import Block

class MapLoader():
    
    def load_map(self,scene,maps,number):
        
        self.file = open(maps[number],"r")
        self.scene = scene
        
        self.map = False
        self.title = False
        
        self.map_info = {'xsize':0,'ysize':0,'currentlevel':number}
        self.lava_group = []
        
        self.current_line = ''
        
        while True:
            if self.current_line.startswith("#"):
                self.current_line = self.current_line.strip()
                self.current_line = self.current_line.lower()
            else:
                self.current_line = self.file.readline()
                if self.current_line == "":
                    break
                else:
                    self.current_line = self.current_line.strip()
                    self.current_line = self.current_line.lower()
                    
            if self.current_line == "":
                pass
            elif self.current_line == "#title":
                self.titlereader()
                self.title = True
                
            elif self.current_line == "#map":
                self.mapreader()
                self.map = True
                
            else:
                pass
            
        if self.map and self.title:
            for lava in self.lava_group:
                lava.animation.reset_animation()
            
            return self.map_info
        else:
            print("Map information missing.")
                
    
    def titlereader(self):
        
        while True:
            self.current_line = self.file.readline()
            if self.current_line == "" or self.current_line.startswith("#"):
                break
            else:
                self.current_line = self.current_line.strip()
                self.current_line = self.current_line.lower()
                
                if self.current_line == "":
                    pass
                else:
                    info = self.current_line.split("=")
                    if len(info) != 2:
                        pass
                    else:
                        if info[0].strip() == "name":
                            self.map_info['name'] = info[1].strip()
                        elif info[0].strip() == "backgroundgradient":
                            gradients = info[1].split("-")
                            gradient1 = gradients[0].split(",")
                            gradient2 = gradients[1].split(",")
                            
                            gradient1 = list(map(int, gradient1))
                            gradient2 = list(map(int, gradient2))
                            
                            self.map_info['background'] = [gradient1,gradient2]
                            
                        elif info[0].strip() == "backgroundpixmap":
                            self.map_info['backgroundpixmap'] = info[1].strip()
                            
    def mapreader(self):
        
        y=0
        while True:
            self.current_line = self.file.readline()
            if self.current_line == "" or self.current_line.startswith("#"):
                break
            else:
                self.current_line = self.current_line.strip()
                
                if self.current_line == "":
                    pass
                else:
                    y+=1
                    row = self.current_line.split(":")
                    self.map_info['xsize'] = len(row)*32
                    x=0
                    for block in row:
                        if block == "0":
                            pass
                        elif block == "g":
                            block = Block(x,y,self.scene,"Textures/Blocks/BlockGrass.png")
                        elif block == "d":
                            block = Block(x,y,self.scene,"Textures/Blocks/BlockGround.png")
                        elif block == "s":
                            block = Block(x,y,self.scene,"Textures/Blocks/BlockRock.png")
                        elif block == "X":
                            derbiili = Derbiili(x,y,self.scene)
                            self.scene.addItem(derbiili)
                            self.scene.addDerbiili(derbiili)
                        elif block == "C":
                            item = Cake(x,y)
                            self.scene.addItem(item)
                        elif block == "G":
                            item = Flower(x,y)
                            self.scene.addItem(item)
                        elif block == "M":
                            block = Spikes(x,y,self.scene)
                        elif block == "b":
                            block = Block(x,y,self.scene,"Textures/Blocks/BlockBox.png")
                        elif block == "I":
                            block = BlockIce(x,y,self.scene)
                        elif block == "p":
                            block = Platform(x,y,self.scene)
                        elif block == "D":
                            block = Block(x,y,self.scene,"Textures/Blocks/BlockDeadGrass.png")
                        elif block == "P":
                            block = Portal(x,y,self.scene)
                        elif block == "L":
                            block = Lava(x,y,self.scene)
                            self.lava_group.append(block)
                        elif block == "l":
                            block = Lava(x,y,self.scene,flow_direction='vertical')
                            self.lava_group.append(block)
                        elif block == "&":
                            block = Checkpoint(x,y,self.scene)
                        elif block == "K":
                            block = Crown(x,y)
                            self.scene.addItem(block)
                        elif block == "1":
                            enemy = Snake(x,y,self.scene)
                        elif block == "2":
                            enemy = Bat(x,y,self.scene)
                        elif block == "3":
                            enemy = CaveBug(x,y,self.scene)
                        elif block == "4":
                            enemy = Ghost(x,y,self.scene)
                        
                        
                        
                        x+=1
        
        self.map_info['ysize'] = y*32
        