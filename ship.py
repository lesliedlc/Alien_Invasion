'''
Overview: Draw the players ship on the screen. 
'''
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    ## A class to manage the ship ##


    def __init__(self, ai_game): # (self reference, reference to AI class)
        ## Initialize the ship and set its starting position ##
        
        super().__init__()
        ## ASSIGN ATTRIBUTES TO SHIP ##
        self.screen = ai_game.screen # assign screen
        self.settings = ai_game.settings # assign settings
        self.screen_rect = ai_game.screen.get_rect() # rect means rectangles, access the screen rect

        ## LOAD SHIP IMAGE & GET RECT ##
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # ships surface

        self.rect.midbottom = self.screen_rect.midbottom # start at middle bottom
        self.x = float(self.rect.x) # store decimal value for horizontal positon

        ## MOVEMENT FLAG L/R NO MOVEMENT ##
        self.moving_right = False
        self.moving_left = False


    def update(self): # Not considered helper method bc called through ship
    
        ## MOVEMENT FLAG TRUE - MOVE CONTINIOUSLY L/R ##
        ## KEEPS SHIP ON SCREEN ##
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed # updates x value not rect
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        ## Draw the bottom of the ship at its current location ##
        ## DRAW IMAGE @ SPECIFIED RECT ##
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        ## Center the ship on the screen ##
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

