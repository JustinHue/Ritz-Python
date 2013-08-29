'''
Created on Aug 27, 2013

@author: Justin Hellsten
'''

import pygame
pygame.init()

FALLING = "falling"
IDLE = "idle"
JUMPING = "jumping"
WALK = "walk"

RITZ_FALLING_MAX = 2
RITZ_IDLE_MAX = 4
RITZ_JUMPING_MAX = 2
RITZ_WALK_MAX = 5

"""
    Directory Constants
"""
GFX_DIR = "gfx/"
SFX_DIR = "sfx/"
MFX_DIR = "mfx/"
RITZ_DIR = GFX_DIR + "ritz/"

"""
    Map data file constants
"""
INSTRUCTIONS_MAP = "instructions.dat"
START_SCREEN_MAP = "startscreen.dat"


"""
    Image/Graphic Constants
"""
IMG_SPLASH_SCREEN = pygame.image.load(GFX_DIR + "splashscreen.png")
IMG_RITZ_SPRITES = {FALLING:[pygame.image.load(RITZ_DIR + FALLING + "{0}.png".format(x)) \
                             for x in range(RITZ_FALLING_MAX)],
                    IDLE:[pygame.image.load(RITZ_DIR + IDLE + "{0}.png".format(x)) \
                             for x in range(RITZ_FALLING_MAX)],
                    JUMPING:[pygame.image.load(RITZ_DIR + JUMPING + "{0}.png".format(x)) \
                             for x in range(RITZ_FALLING_MAX)],
                    WALK:[pygame.image.load(RITZ_DIR + WALK + "{0}.png".format(x)) \
                             for x in range(RITZ_FALLING_MAX)],}

"""
    Scene Constants
"""
# --- Splash Scene --- #
SPLASH_SCENE_WIDTH = 800
SPLASH_SCENE_HEIGHT = 600
SPLASH_SCENE_CAPTION = "Hellsten Inc"
SPLASH_SCENE_FLAGS = 0
SPLASH_SCENE_DEPTH = 0

INSTRUCTIONS_SCENE_WIDTH = 800
INSTRUCTIONS_SCENE_HEIGHT = 600
INSTRUCTIONS_SCENE_CAPTION = "How to play"
INSTRUCTIONS_SCENE_FLAGS = 0
INSTRUCTIONS_SCENE_DEPTH = 0

START_SCENE_WIDTH = 800
START_SCENE_HEIGHT = 600
START_SCENE_CAPTION = "Ritz - Version 1.0"
START_SCENE_FLAGS = 0
START_SCENE_DEPTH = 0

PLAY_SCENE_WIDTH = 800
PLAY_SCENE_HEIGHT = 600
PLAY_SCENE_CAPTION = ""
PLAY_SCENE_FLAGS = 0
PLAY_SCENE_DEPTH = 0

CREDITS_SCENE_WIDTH = 800
CREDITS_SCENE_HEIGHT = 600
CREDITS_SCENE_CAPTION = "Damn you. Sincerly, the Hellsten family"
CREDITS_SCENE_FLAGS = 0
CREDITS_SCENE_DEPTH = 0

