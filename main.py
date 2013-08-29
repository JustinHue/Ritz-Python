'''
Created on Aug 26, 2013

@author: justin
'''

import gameScenes

def main():
    
    """
        Set up splash scene
    """
    splashScene = gameScenes.SplashScene()
    instructionScene = gameScenes.InstructionScene()
    startScene = gameScenes.StartScene()
    playScene = gameScenes.PlayScene()
    creditScene = gameScenes.CreditScene()
    
    splashScene.prepare()

    """
        Misc. Init
    """
    currentScene = splashScene
    isRunning = True
    
    """
        Game Loop
    """
    while (isRunning):
        state = currentScene.run()
        if (state == currentScene.ON_QUIT):
            isRunning = False     
        else:   
            if (currentScene == splashScene):
                if (state == currentScene.ON_KEYDOWN):
                    currentScene = instructionScene
                    instructionScene.prepare()
            elif (currentScene == instructionScene):
                pass
            elif (currentScene == startScene):
                pass
            elif (currentScene == playScene):
                pass
            elif (currentScene == creditScene):
                pass

if __name__ == "__main__": 
    main()
    
