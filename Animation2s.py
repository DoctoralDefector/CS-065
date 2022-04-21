#author: your name here
#date: 
#description: provide a brief description of your program
#proposed points (out of 10): a description of the number 
#of points you believe your assignment is worth.
from Spaceship import *
from Ball import *
from tkinter import *

class Animation:
    def __init__(self):
        window = Tk()
        window.title("CS 65") # Set a title

        # establish the canvas
        self.width = 600 # Width of the self.canvas
        self.height = 400 # Height of the self.canvas
        self.canvas = Canvas(window, bg = "white",
            width = self.width, height = self.height)
        self.canvas.pack()

        # create a spaceship
        self.spaceship = Spaceship(self.canvas, 200, 380, "black")
        window.bind("<Motion>", self.move_spaceship)

        # create an empty list
        self.ball_list = []
        
        self.add_ball()

        # start the animation loop
        # The call to self.animate() should be the last line in the __init__function.
        self.animate()

    def move_spaceship(self, event):
        self.spaceship.x = event.x - self.spaceship.width/2
        print("mouse position:", event.x, event.y)
        
    def add_ball(self):
        # create a ball and add it to the list
        diameter = 30
        start_x = random.randint(0,self.width-diameter)
        start_y = random.randint(0,self.height/2) # top half of screen
        ball = Ball(self.canvas, start_x, start_y, "red", diameter)
        self.ball_list.append(ball)

    # animation
    def animate(self):
        frame = 0
        while True:
            self.canvas.after(20) # Sleep
            self.canvas.update() # Update self.canvas
            frame += 1
            if len(self.ball_list) == 0:
                # game over
                break
                
            self.spaceship.draw()
            
            if frame %100 == 0:
                self.add_ball()
            
            # loop through all of the items in the list
            # move the ball and draw it
            for b in self.ball_list:
                b.move()
                b.draw()
                #if ball hits the spaceship, make it bounce off the spaceship
                if self.spaceship.overlap(b):
                    b.bounce_vert()
                
                #if ball hits the bottom; remove it from the list 
                if b.hit_bottom():
                    self.ball_list.remove(b)
        
            
        
Animation()

