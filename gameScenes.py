'''
Created on Aug 26, 2013

@author: justin
'''

import gameEngine
import gameSprites
import gameConstants

class SplashScene(gameEngine.scene.Scene):
    def __init__(self):
        gameEngine.scene.Scene.__init__(self, 
                                        gameConstants.SPLASH_SCENE_WIDTH, 
                                        gameConstants.SPLASH_SCENE_HEIGHT, 
                                        gameConstants.SPLASH_SCENE_CAPTION,
                                        gameConstants.SPLASH_SCENE_FLAGS,
                                        gameConstants.SPLASH_SCENE_DEPTH)
        
        self.splashImage = gameSprites.SplashSprite((self.width / 2, 
                                                     self.height / 2))
        self.ritzImage = gameSprites.RitzSprite((100, 100))
         
        self.sprites.append(self.splashImage)
        self.sprites.append(self.ritzImage)
        
class InstructionScene(gameEngine.scene.Scene):
    def __init__(self):
        gameEngine.scene.Scene.__init__(self, 
                                        gameConstants.INSTRUCTIONS_SCENE_WIDTH, 
                                        gameConstants.INSTRUCTIONS_SCENE_HEIGHT, 
                                        gameConstants.INSTRUCTIONS_SCENE_CAPTION,
                                        gameConstants.INSTRUCTIONS_SCENE_FLAGS,
                                        gameConstants.INSTRUCTIONS_SCENE_DEPTH)
        
        
class StartScene(gameEngine.scene.Scene):
    def __init__(self):
        gameEngine.scene.Scene.__init__(self, 
                                        gameConstants.START_SCENE_WIDTH, 
                                        gameConstants.START_SCENE_HEIGHT, 
                                        gameConstants.START_SCENE_CAPTION,
                                        gameConstants.START_SCENE_FLAGS,
                                        gameConstants.START_SCENE_DEPTH)
        
class PlayScene(gameEngine.scene.Scene):
    def __init__(self):
        gameEngine.scene.Scene.__init__(self, 
                                        gameConstants.PLAY_SCENE_WIDTH, 
                                        gameConstants.PLAY_SCENE_HEIGHT, 
                                        gameConstants.PLAY_SCENE_CAPTION,
                                        gameConstants.PLAY_SCENE_FLAGS,
                                        gameConstants.PLAY_SCENE_DEPTH)
        
class CreditScene(gameEngine.scene.Scene):
    def __init__(self):
        gameEngine.scene.Scene.__init__(self, 
                                        gameConstants.CREDITS_SCENE_WIDTH, 
                                        gameConstants.CREDITS_SCENE_HEIGHT, 
                                        gameConstants.CREDITS_SCENE_CAPTION,
                                        gameConstants.CREDITS_SCENE_FLAGS,
                                        gameConstants.CREDITS_SCENE_DEPTH)
        
        