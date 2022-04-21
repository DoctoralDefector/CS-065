# name: T. Urness
# description: A Ball Class, inherits from Shape
# The Ball class keeps track of position, diameter, speed, and going_up values for a Ball

from Shape import *
import pygame
import tkinter


class Ball(Shape):

    # initialization method
    # x -- x position of upper left corner of ball
    # y -- y poisition of upper left corner of ball
    # color -- string; color of ball to be drawn
    # diameter -- diameter of ball
    # canvas -- window canvas, part of tkinter
    def __init__(self,  canvas, x, y, color, diameter): 
        self.img = tkinter.PhotoImage(file="covid.png") #switches ball image to covid image
        Shape.__init__(self,canvas, x, y,diameter, diameter, color) #sets location and diamter of ball
        self.speed_x = 6 #speed of ball in x direction
        self.speed_y = 6 #speed of ball in y direction

    def move(self):
        # update ball values for x and y update according to speed
        # bounce ball off of walls
        
        self.x += self.speed_x #updates ball speed in x direciton
        self.y += self.speed_y #updates balls speed in y direction
        
        if self.x + self.width > self.canvas.winfo_width() or self.x < 0: 
            self.speed_x = -self.speed_x #sets the ball within the canvas width
        
        if self.y + self.height > self.canvas.winfo_height() or self.y < 0:
            self.speed_y = -self.speed_y #sets the ball within the canvas height
    
    def bounce_vert(self):
        # bounce vertically
        self.speed_y = -self.speed_y #bounces the ball in the opposite direction with same relative speed

    def draw(self):
        #draw the ball
        self.canvas.delete("ball"+str(self.id)) #deletes ball image
        self.canvas.create_image(self.x + self.width/2, self.y +self.height/2,
                                 image = self.img, tags = "ball" + str(self.id)) #creates a new ball image
        
                                
