'''
Created on Aug 27, 2013

@author: justin
'''

import pygame
import color
pygame.init()
    
class Map(pygame.sprite.Sprite):
    def __init__(self, scene, filepath):
        pygame.sprite.Sprite.__init__(self)
        self.mapfile = open(filepath, 'r')
        self.data = {}
        self.scene = scene
        self.image = pygame.surface.Surface((self.scene.width, self.scene.height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.loadMap(filepath)
        self.scroll = (0.0, 0.0)
        self.scenesize = (self.scene.width, self.scene.height)
        
    def loadMap(self, filepath):
        currentSection = ""
        """
            Parse Map data using section => data configuration
            Eg. 
            [Section]
            data
            data
            [Another_Section]
            Other Data
            Other Data
        """
        for line in self.mapfile.readlines():
            line = line.strip()
            if (line.find('[') != -1 and line.find(']') != -1):
                self.data[line] = []
                currentSection = line
            elif (line != ""):
                self.data[currentSection].append(line)
                
    def setScrollPosition(self, x, y):
        """
            Map boundary scroll check
        """
        if (x < 0):
            x = 0
        elif (x + self.scenesize[0] > self.mapsize[0]):
            x = self.mapsize[0] - self.scenesize[0]
            
        if (y < 0):
            y = 0
        elif (y + self.scenesize[1] > self.mapsize[1]):
            y = self.mapsize[1] - self.scenesize[1]
            
        self.scroll = (x, y)
                        
    def doEvent(self, event):
        pass
    
    def update(self):
        pass
    
    
class TileMap(Map):
    TILES = "[tiles]"
    ENTITIES = "[entities]"
    TILESIZE = "[tilesize]"
    TILEIMGS = "[tileimgs]"
    TILEDIR = "[tiledir]"
    def __init__(self, scene, filepath):
        self.tiles = []
        self.entities = []
        self.tilesize = []
        self.tileimages = []
        self.size = []
        self.mapsize = []
        self.tiledir = ""
        Map.__init__(self, scene, filepath)
        self.scenets = (self.scenesize[0] / self.tilesize, self.scenesize[1] / self.tilesize)
        self.render()
        

    def loadMap(self, filepath):
        Map.loadMap(self, filepath)
        
        """
            Parse tiles data into tiles 2d array
        """
        for tileData in self.data[self.TILES]:
            row = []
            self.tiles.append(row)
            for token in tileData.split(','):
                row.append(int(token))
                
        """
            Parse tile size data
        """
        self.tilesize = int(self.data[self.TILESIZE][0])
        
                        
        """
            Parse map size (based on tiles data)
        """
        self.size = (len(self.tiles[0])), len(self.tiles)
        self.mapsize = (self.size[0] * self.tilesize, self.size[1] * self.tilesize)
        
        """
            Parse Entity data into entities list
        """
        for entityData in self.data[self.ENTITIES]:
            tokens = entityData.split(',')
            self.entities.append(tokens)
        
        """
            Parse tile directory
        """
        self.tiledir = self.data[self.TILEDIR][0]
        
        """
            Parse tile image data
        """
        for imagepath in self.data[self.TILEIMGS]:
            self.tileimages.append(pygame.image.load(self.tiledir + imagepath))
            
    def getTileAt(self, ix, iy):
        return self.tiles[iy][ix]
    
    def getTileImage(self, tileindex):
        return self.tileimgs[tileindex]        
                
    def setScrollPosition(self, x, y):
        Map.setScrollPosition(self, x, y)
        self.render()
        
    def render(self):
        """
            Clear map
        """
        self.image.fill((color.BLACK))
        
        """
            Define scroll, offsets, blitoffset variables to render
            tiles according to scroll position values.
        """
        scrollix = int(self.scroll[0] / self.tilesize)
        scrolliy = int(self.scroll[1] / self.tilesize)
        offSetX = self.scroll[0] % self.tilesize
        offSetY = self.scroll[1] % self.tilesize
        imgSetY = 0
        blitOffSetY = 0
        blitOffSetX = 0

 
            
        """
            Commence with rendering of tiles
        """            
        for rowCount in range(scrolliy, scrolliy + self.scenets[1]):
            imgSetX = 0
            for columnCount in range(scrollix, scrollix + self.scenets[0]):
                blitRect = pygame.rect.Rect((blitOffSetX, blitOffSetY), (self.tilesize, self.tilesize))
                self.image.blit(self.tileimages[self.tiles[rowCount][columnCount]], 
                                (imgSetX, imgSetY), blitRect)
                imgSetX += self.tilesize
            imgSetY += self.tilesize

        """
        for rowCount in range(scrolly, scrolly + sceneyts):
            imgSetX = 0
            blitOffSetX = offSetX
            for columnCount in range(scrollx, scrollx + scenexts):
                blitRect = pygame.rect.Rect((blitOffSetX, blitOffSetY), (self.tilesize, self.tilesize))
                self.image.blit(self.tileimages[self.tiles[rowCount][columnCount]], 
                                (imgSetX, imgSetY), blitRect)
                # Redefine blit/offsets for next column iteration (are we dealing with
                # first column or any other column). First columns may or may not have blit offset.
                if (columnCount != 0 or offSetX == 0):            
                    imgSetX += self.tilesize
                    blitOffSetX = 0
                else:
                    imgSetX += offSetX
            # Redefine blit/offsets for next row iteration (are we dealing with
            # top row or any other row). Top rows may or may not have blit offset.
            if (rowCount != 0 or offSetY == 0):
                imgSetY += self.tilesize
                blitOffSetY = 0
            else: 
                imgSetY += offSetY

        """
        
    def doEvent(self, event):
        pass

    def update(self):
        pass
    
