#author: Blake Gerold
#date: Nov 17, 2020
#description: Corona envader is an avoid and shoot target based game similar to space invader
#             except the enemy is cornavirus and the spaceship shoots vaccines
#proposed points (10 of 10): (6): Implemented a game that
#                            (1) game is "orginal",
#                            (1) have multipl balls
#                            (1) used sounds and images for the paddle and balls
#                            (1) Has game over displayed when player loses
                                  

from Paddle import *
from Ball import *
from pewpewvaccine import *
from tkinter import *

class Animation:
    def __init__(self):
        """Purpose: creates a funtion that can be applied across the class
       
       Paramters: self
       
       Return: none
       
       Preconditions: Paddle, ball, pewpewvaccine and tkinter properly imported
       
       Postconditions: provide values for other funtions
        """
        window = Tk()
        window.title("Corona Evader") # Set a title
        
        pygame.init()
        
        # establish the canvas
        self.width = 600 # Width of the self.canvas
        self.height = 400 # Height of the self.canvas
        self.canvas = Canvas(window, bg = "black", #sets the color of the canvas to black
            width = self.width, height = self.height)
        self.canvas.pack()

        # create a paddle
        self.paddle = Paddle(self.canvas, 300, 380, "black") #sets the spaceships starting location
        self.currentx = 200 #set the starting x at 200 because that is where the ships starts
        window.bind("<Motion>", self.move_paddle) #binds the ship to the bottom of the canvas and left/right movement
        window.bind("<KeyPress-space>", self.add_shots) #allows the player to shoot vaccines

        # create an empty list
        self.ball_list = [] #a list of all the corona virus enemies
        
        self.add_ball() #executes the add ball function
        
        self.shots_list = [] #a list of all the shots fired by the player enemies
        
        # start the animation loop
        # The call to self.animate() should be the last line in the __init__function.
        self.animate()

    def move_paddle(self, event):
        """Purpose: sets the spaceship to move left and right and given an event location
       
       Paramters: self, event
       
       Return: none
       
       Preconditions: __init__ executed properly, Paddle is imported
       
       Postconditions: allows moves the paddle left and right on the canvas
        """
        self.paddle.x = event.x - self.paddle.width/2 #sets center fot he paddle to the mouse position
        self.currentx = event.x #records currentx to be the center of the paddle as well
#         print("mouse position:", event.x, event.y)
        
    def add_ball(self):
        # create a ball and add it to the list
        """Purpose: adds balls to canvas when called
       
       Paramters: self
       
       Return: none
       
       Preconditions: __init__ executed properly, ball is imported
       
       Postconditions: creates ball object when called 
        """
        diameter = 50 #ball diamter
        start_x = random.randint(0,self.width-diameter) #random x postion for the ball
        start_y = random.randint(0,(self.height/2)) # top half of screen for the y postion
        ball = Ball(self.canvas, start_x, start_y, "red", diameter) #sets the starting postion, color and size of the ball
        self.ball_list.append(ball) #adds new balls the the ball list
        
    def add_shots(self, event):
        """Purpose: fires shots from the space ship
       
       Paramters: self, event
       
       Return: none?
       
       Preconditions: __init__ executed properly, pewpewvaccine is imported
       
       Postconditions: creates a shots when called
        """
        event = 0 #starts events at 0
        self.sound = pygame.mixer.Sound("eleclaser.wav") #makes firing sounds when executes
        pygame.mixer.Sound.play(self.sound) #sound mixer through the pygame package
        shots = pewpewvaccine(self.canvas, self.currentx, 374, "red") #sets shots for the pewpewvaccine funtion
        self.shots_list.append(shots) #adds shots to the shots_list
    

    def animate(self):
        """Purpose: combines all the previous functions into one.
       
       Paramters: self
       
       Return: none
       
       Preconditions: __init__, move_paddle, add_ball, add_shots execute properly
       
       Postconditions: animates all the funtions on a canvas for spaceship, corona virus balls, score, gameover and vaccines
        """
        score = 0 #starts score at 0
        frame = 0 #starts frames at 0
        difficulty = 0 #starts difficulty at zero
        while True: #while loop that keeps the game going
            self.canvas.after(20) # Sleep
            self.canvas.update() # Update self.canvas
            self.canvas.delete("score") #allows the score to be update
            self.canvas.create_text(525, 40, text="Score: " + str(score), #creates a score board
                                    font=("Helvetica", 30),
                                    fill="white", tags="score")
            frame += 1 #adds one to the total frame
                 
            self.paddle.draw() #draws the paddle
            
            
            if frame %(100 - difficulty) == 0: #spawns the balls quicker with increasing speed
                self.add_ball() #excutes the add_ball funciton
            
            # loop through all of the items in the list
            # move the ball and draw it
            for b in self.ball_list: #loops through the ball list
                b.move() #moves the ball
                b.draw() #draws the

                for s in self.shots_list: #loops through shots_list
                    s.move() #moves shots
                    s.draw() #draws shots
                    if s.overlap(b): #if shots overlap balls excutes
                        self.ball_list.remove(b) #remove balls
                        self.shots_list.remove(s) #removes shots
                        self.sound = pygame.mixer.Sound("coronadeath.wav") #access sound file
                        pygame.mixer.Sound.play(self.sound) #excutes explosion sounds
                        score +=1 #adds 1 to the score
                        if score < 100: #if score is less then 100
                            difficulty += 1 #adds on to the difficutly to make balls spawn more often
                        
            if self.paddle.overlap(b): #if the paddle overlaps with a ball
                self.sound = pygame.mixer.Sound("gameoversfx.wav") #access this file
                pygame.mixer.Sound.play(self.sound) #play plays the gameover sound
                self.canvas.create_text(300, 200, text="Game Over", #gameover location on canvas
                                        font=("Helvetica", 60),
                                        fill="red", tags="gameOver")
                break #stops the game


                

                      
Animation() #excutes animation
