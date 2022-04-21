from Shape import *
import pygame
import tkinter

class pewpewvaccine(Shape): #used to create vaccine animation
    def __init__(self, canvas, x, y, color):
        """Purpose: creates a function that can be applied across the class
       
           Paramters: self, canvas, x, y, color
       
           Return: none
       
           Preconditions: Shape, pygame and tkinter are imported     
           
           Postconditions: provide values for other funtions
        """
        self.img = tkinter.PhotoImage(file="shots.png") #sets the shape as a shot image
        Shape.__init__(self, canvas, x, y, 8, 26, color) #location and shape of shot on canvas
        self.speed_y = -10 #shot speed shooting upward
        self.speed_x = 0 #shot only moves straigh forwad
    
    def move(self):
        """Purpose: updates the location of the shots hit box
       
           Paramters: self
       
           Return: none
       
           Preconditions: Shape, pygame and tkinter are imported, __init__ executes correctly     
           
           Postconditions: updates the hit box location of the shots.png and provide a shooting sound
        """
        self.sound = pygame.mixer.Sound("eleclaser.wav") #creats a shot sound when executed
        self.x += self.speed_x #updates the shot x location
        self.y += self.speed_y #updates the shot y location
        
        
    def draw(self):
        """Purpose: destory and creates the shots.png over and over
       
           Paramters: self
       
           Return: none
       
           Preconditions: Shape, pygame and tkinter are imported, __init__ executes correctly    
           
           Postconditions: creates and destroy images the shots.png over and over
        """
        self.canvas.delete("pewpewvaccine"+str(self.id)) #deletes the image created
        self.canvas.create_image(self.x + self.width/2, self.y + self.height/2,
                                image = self.img, tags="pewpewvaccine"+str(self.id)) #creates the shot image