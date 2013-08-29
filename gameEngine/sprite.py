'''
Created on Aug 24, 2013

@author: justin
'''

import pygame
import math

class StaticSprite(pygame.sprite.Sprite):
    def __init__(self, center, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def doEvent(self, event):
        pass
    
    def update(self):
        pass
        
    def changeImage(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
    def setCenterPosition(self, (center)):
        self.rect.center = center
        
        
class DynamicSprite(StaticSprite):
    def __init__(self, center, image, speed=0, angle=0):
        StaticSprite.__init__(self, center, image)
        self.speed = speed

        self.cx = self.rect.centerx
        self.cy = self.rect.centery
                
        self.setAngle(angle)
        self.__calcComponents()
        

    def doEvent(self, event):
        pass
    
    def update(self):
        self.cx += self.dx
        self.cy += self.dy
        
    def setSpeed(self, speed):
        self.speed = speed
        self.__calcComponents()
        
    def setAngle(self, angle):
        self.angle = angle
        self.radians = math.radians(self.angle)
        
    def __calcComponents(self):
        self.dx = self.speed * math.sin(self.radians) 
        self.dy = self.speed * math.cos(self.radians) * -1
                
        