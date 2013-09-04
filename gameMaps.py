'''
Created on Aug 27, 2013

@author: justin
'''

import gameEngine
import gameConstants

class RitzTileMap(gameEngine.maps.TileMap):
    def __init__(self, scene, filepath):
        gameEngine.maps.TileMap.__init__(self, scene, filepath)
        
        
class InstructionsMap(RitzTileMap):
    def __init__(self, scene):
        RitzTileMap.__init__(self, scene, gameConstants.INSTRUCTIONS_MAP)
        
    
    
    
    
    

        
        
