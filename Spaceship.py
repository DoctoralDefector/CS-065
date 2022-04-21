from Shape import *
import pygame
import tkinter

class Spaceship(Shape):
    def __init__(self, canvas, x, y, color):
        self.img = tkinter.PhotoImage(file="spaceship.png")
    
    def draw(self):
        self.canvas.delete("spaceship"+str(self.id))
        self.canvas.create_image(self.x, self.y, self.x + self.width,
                                     self.y + self.height, fill=self.color,
                                     tags="spaceship"+str(self.id))
