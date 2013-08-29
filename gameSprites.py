'''
Created on Aug 27, 2013

@author: Justin Hellsten
'''

import gameEngine
import gameConstants

class SplashSprite(gameEngine.sprite.StaticSprite):
    def __init__(self, center):
        gameEngine.sprite.StaticSprite.__init__(self, 
                                                center, 
                                                gameConstants.IMG_SPLASH_SCREEN)
        
class RitzSprite(gameEngine.sprite.DynamicSprite):
    def __init__(self, center):
        gameEngine.sprite.DynamicSprite.__init__(self, 
                                                 center,
                                                 gameConstants.IMG_RITZ_SPRITES[gameConstants.IDLE][0])
        
    def update(self):
        gameEngine.sprite.DynamicSprite.update(self)
        
    def doEvent(self, event):
        gameEngine.sprite.DynamicSprite.doEvent(self, event)

 