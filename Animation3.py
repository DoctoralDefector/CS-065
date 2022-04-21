#author: your name here
#date: 
#description: provide a brief description of your program
#proposed points (out of 10): a description of the number 
#of points you believe your assignment is worth.
from Paddle import *
from Ball import *
from pewpewvaccine import *
from tkinter import *

class Animation:
    def __init__(self):
        event = 0
        window = Tk()
        window.title("Corona Evader") # Set a title
        
        pygame.init()
        
        # establish the canvas
        self.width = 600 # Width of the self.canvas
        self.height = 400 # Height of the self.canvas
        self.canvas = Canvas(window, bg = "darkblue",
            width = self.width, height = self.height)
        self.canvas.pack()

        # create a paddle
#        self.paddle = Paddle(self.canvas, 200, 380, "black")
        self.paddle = Paddle(self.canvas, 50, 380, "black")
        self.currentx = 0
        window.bind("<Motion>", self.move_paddle)
        window.bind("<KeyPress-space>", self.add_shots)

        # create an empty list
        self.ball_list = []
        
        self.add_ball()
        
        self.shots_list = []
        
        # start the animation loop
        # The call to self.animate() should be the last line in the __init__function.
        self.animate()

    def move_paddle(self, event):
        self.paddle.x = event.x - self.paddle.width/2
        self.currentx = event.x
#         print("mouse position:", event.x, event.y)
        
    def add_ball(self):
        # create a ball and add it to the list
        diameter = 70
        start_x = random.randint(0,self.width-diameter)
        start_y = random.randint(0,self.height/2) # top half of screen
        ball = Ball(self.canvas, start_x, start_y, "red", diameter)
        self.ball_list.append(ball)
        
    def add_shots(self, event):
        #need to define in __init_
        #self.pewpewvaccine.x = event.x - self.paddle.width/2
        shots = pewpewvaccine(self.canvas, self.currentx, 374, "red")
        self.shots_list.append(shots)
    

    def animate(self):
        score = 0
        frame = 0
        difficulty = 0
        while True:
            self.canvas.after(20) # Sleep
            self.canvas.update() # Update self.canvas
            frame += 1
#             if len(self.ball_list) == 0:
# #                 # game over
#                 break
#             if self.paddle.overlap(b):
#                 break
                 
            self.paddle.draw()
            
            
            if frame %(100 - difficulty) == 0:
                self.add_ball()
            # loop through all of the items in the list
            # move the ball and draw it
            for b in self.ball_list:
                b.move()
                b.draw()

                #if ball hits the bottom; remove it from the list 
#                 if self.ball.overlap(b):
#                     self.ball_list.remove(b)
#                     self.shots.remove(s)
#             
                for s in self.shots_list:
                    s.move()
                    s.draw()
                    if s.overlap(b):
                        self.ball_list.remove(b)
                        self.shots_list.remove(s)
                        score += 1
                        difficulty += 1
                        #print(score)
            if self.paddle.overlap(b):
                     break
                
                #if ball hits the paddle, make it bounce off the paddle
#                 if self.paddle.overlap(b):
#                     b.bounce_vert()
                    
                #if ball hits the bottom; remove it from the list

                

                      
Animation()