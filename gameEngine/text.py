'''
Created on Aug 24, 2013

@author: justin
'''

import pygame
import color
import math

class Text(pygame.sprite.Sprite):
    DEFAULT_SIZE = 18
    DEFAULT_BOLD = False
    DEFAULT_ITALIC = False
    DEFAULT_COLOR = color.ALICE_BLUE
    DEFAULT_NAME = "Helvetica"
    DEFAULT_ANTIALIAS = True
    DEFAULT_BACKGROUND_RGBA = (0,0,0,0)
    def __init__(self, center, text):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.size = self.DEFAULT_SIZE
        self.bold = self.DEFAULT_BOLD
        self.italic = self.DEFAULT_ITALIC
        self.color = self.DEFAULT_COLOR
        self.name = self.DEFAULT_NAME
        self.antialias = self.DEFAULT_ANTIALIAS
        self.background = self.DEFAULT_BACKGROUND_RGBA
        self.font = pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
        self.image = self.font.render(self.text, self.antialias, self.color, self.background)
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def update(self):
        pass
    
    def doEvent(self):
        pass
    
    def __render(self):
        self.font = pygame.font.SysFont(self.name, self.size, self.bold, self.italic)
        self.image = self.font.render(self.text, self.antialias, self.color, self.background)
        originalCenter = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = originalCenter
        
    def setText(self, text):
        self.text = text
        self.__render()
        
    def setCenterPosition(self, (center)):
        self.rect.center = center

    def setFontSize(self, size):
        self.size = size
        self.__render()
        
    def makeBold(self, flag):
        self.bold = flag
        self.__render()
        
    def makeItalic(self, flag):
        self.italic = flag
        self.__render()
        
    def setColor(self, color):
        self.color = color
        self.__render()
        
    def setName(self, name):
        self.name = name
        self.__render()
        
    def setAntialias(self, flag):
        self.antialias = flag
        self.__render()
        
    def setBackground(self, background):
        self.background = background
        self.__render()
        

class DynamicText(Text):
    def __init__(self, center, text, speed, angle):
        Text.__init__(self, center, text)
        self.speed = speed
        self.angle = angle
        self.radians = math.radians(self.angle)
        self.dx = self.speed * math.sin(self.radians) 
        self.dy = self.speed * math.cos(self.radians) * -1
        self.cx = self.rect.centerx
        self.cy = self.rect.centery
        
    def update(self):
        self.cx += self.dx
        self.cy += self.dy
        
    def doEvent(self, event):
        pass
    

class CreditText(DynamicText):
    def __init__(self, center, text, speed=1, angle=0):
        DynamicText.__init__(self, center, text, speed, angle)
        
    def update(self):
        DynamicText.update(self)
        
    def doEvent(self, event):
        DynamicText.doEvent(self, event)
        
        
class CreditSection(pygame.sprite.Group):
    NAME_SPACE = 25
    DEFAULT_COLOR = color.AIR_FORCE_BLUE
    def __init__(self, center, text, speed=1, angle=0):
        pygame.sprite.Group.__init__(self)
        self.section = CreditText(center, text, speed, angle)
        self.section.setColor(self.DEFAULT_COLOR)
        self.add(self.section)
        self.names = []

    def addName(self, name):
        self.add(name)
        self.names.append(name)
        self.__resetNamePosition()
    
    def __resetNamePosition(self):
        incrementY = self.section.rect.centery
        for name in self.names:
            incrementY += self.NAME_SPACE
            name.setCenterPosition((self.section.rect.centerx, incrementY))
