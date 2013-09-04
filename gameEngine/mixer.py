'''
Created on Aug 29, 2013

@author: justin
'''

import pygame
pygame.init()

def playMusic(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()
    
def playSound(sound):
    pass
