'''
Created on Aug 26, 2013

@author: justin
'''

import gameEngine
import gameMaps
import gameSprites
import gameConstants

class SplashScene(gameEngine.scene.Scene):
    DELAY = 120
    MUSIC_DELAY = 15
    def __init__(self):
        gameEngine.scene.Scene.__init__(self, 
                                        gameConstants.SPLASH_SCENE_WIDTH, 
                                        gameConstants.SPLASH_SCENE_HEIGHT, 
                                        gameConstants.SPLASH_SCENE_CAPTION,
                                        gameConstants.SPLASH_SCENE_FLAGS,
                                        gameConstants.SPLASH_SCENE_DEPTH)
        
        self.splashImage = gameSprites.SplashSprite((self.width / 2, 
                                                     self.height / 2))

        self.sprites.append(self.splashImage)
        
        self.__delayCounter = 0
        

    def update(self):
        self.__delayCounter += 1
        if (self.__delayCounter == self.DELAY):
            self.fadeOut(True)
        elif (self.__delayCounter == self.MUSIC_DELAY):
            gameEngine.mixer.playMusic(gameConstants.MFX_SPLASH_SCREEN)
            
    def doEvent(self, event):
        pass
    
 
class InstructionScene(gameEngine.scene.Scene):
    def __init__(self):
        gameEngine.scene.Scene.__init__(self, 
                                        gameConstants.INSTRUCTIONS_SCENE_WIDTH, 
                                        gameConstants.INSTRUCTIONS_SCENE_HEIGHT, 
                                        gameConstants.INSTRUCTIONS_SCENE_CAPTION,
                                        gameConstants.INSTRUCTIONS_SCENE_FLAGS,
                                        gameConstants.INSTRUCTIONS_SCENE_DEPTH)

        self.tileMap = gameMaps.InstructionsMap(self)
        self.sprites.append(self.tileMap) 
        self.x = 0
        
    def update(self):
        gameEngine.scene.Scene.update(self)
        
        self.x += 1
        self.tileMap.setScrollPosition(0, self.x)
        

    def doEvent(self, event):
        gameEngine.scene.Scene.doEvent(self, event)


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
        
        