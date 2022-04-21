from Shape import *
import pygame
import tkinter

class Paddle(Shape):
#    def __init__(self, canvas, x, y, color):
#        Shape.__init__(self,canvas,x,y,180,20,color)
         
    def __init__(self, canvas, x, y, color):
        """Purpose: creates a function that can be applied across the class
       
           Paramters: self, canvas, x, y, color
           
           Return: none
       
           Preconditions: Shape, pygame and tkinter are imported
       
           Postconditions: Creates a spaceship based on a paddle 
        """
        self.img = tkinter.PhotoImage(file="spaceship.png") #sets a ship to be the paddle image
        Shape.__init__(self, canvas, x, y, 50, 50, color) #sets the location and size of ship

    def draw(self):
        """Purpose: destory and creates the spaceship.png over and over
       
           Paramters: self
       
           Return: none
       
           Preconditions: Shape, pygame and tkinter are imported
       
           Postconditions: deletes and creates the space ship image over a paddle to make it look like it is moving.
        """
        self.canvas.delete("paddle"+str(self.id)) #deletes the image of teh ship
        self.canvas.create_image(self.x + self.width/2, self.y + self.height/2,
                                image = self.img, tags="paddle"+str(self.id)) #creates a new image of the ship.
        