# author: T. Urness
# description: a Simple shape class that establishes:
#              x,y, canvas, width, height, and color
#              also implements an overlap function that will determine
#              if the bounding rectangles of shapes overlap
#              This class is meant to be subclassed -- do not edit this class
# I did not touch this area fyi.
import random
import pygame
import tkinter

class Shape:
        
    def __init__(self, canvas, x, y, width, height, color):
        """ initialization method for a Shape
            establishes, x, y position; width, height, color, and canvas """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.id = random.random()
    
    def overlap(self, s):
        """Returns true if input paramater shape overlaps self shape"""
        l1_x = self.x
        l1_y = self.y
        l2_x = s.x
        l2_y = s.y
        r1_x = self.x + self.width
        r1_y = self.y + self.height
        r2_x = s.x + s.width
        r2_y = s.y + s.height
        
        # If one rectangle is on left side of other
        if l1_x > r2_x or l2_x > r1_x:
            return False
        
        # If one rectangle is above other 
        if(l1_y > r2_y or l2_y > r1_y): 
            return False
    
        return True
    