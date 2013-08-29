'''
Created on Aug 27, 2013

@author: justin
'''

import pygame
pygame.init()
    
class Map():
    def __init__(self, filepath):
        self.mapfile = open(filepath, 'r')
        self.data = {}
        self.loadMap(filepath)
        
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
            line = line.trim()
            if (line.find('[') != -1 and line.find(']') != -1):
                self.data[line] = []
                currentSection = line
            elif (line != ""):
                self.data[currentSection].append(line)
                

class TileMap(Map):
    TILES = "[tiles]"
    ENTITIES = "[entities]"
    TILESIZE = "[tilesize]"
    TILEIMGS = "[tileimgs]"
    def __init__(self, filepath):
        Map.__init__(self, filepath)
        self.tiles = []
        self.entities = []
        self.tilesize = []
        self.tileimages = []
        self.size = []
        self.loadMap()
       
    def loadMap(self, filepath):
        Map.loadMap(filepath)
        
        """
            Parse tiles data into tiles 2d array
        """
        for tileData in self.data[self.TILES]:
            row = []
            self.tiles.append(row)
            for token in tileData.split(','):
                row.append(token)
                
        """
            Parse map size (based on tiles data)
        """
        self.size = (len(self.tiles)), len(self.tiles[0])
        
        """
            Parse Entity data into entities list
        """
        for entityData in self.data[self.ENTITIES]:
            tokens = entityData.split(',')
            self.entities.append(tokens)
            
        """
            Parse tile size data
        """
        self.tilesize = self.data[self.TILESIZE][0].split(',')
        
        """
            Parse tile image data
        """
        for imagepath in self.data[self.TILEIMGS]:
            self.tileimages.append(pygame.image.load(imagepath))
        
    def getTileAt(self, ix, iy):
        return self.tiles[iy][ix]
    
    def getTileImage(self, tileindex):
        return self.tileimgs[tileindex]        
                