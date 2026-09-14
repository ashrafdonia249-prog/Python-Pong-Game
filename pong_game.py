#imported turtle module
import turtle
import random



wind = turtle.Screen() #inialize screen
wind.title("ping bong by donia") #set the title of the window
wind.bgcolor("black") #set the background of the window
wind.setup(width = 800 , height=600) #set the width and hieght of the window
wind.tracer(0) #stops the window from updating automatically

#lPaddle
lPaddle = turtle.Turtle() #intializes turtle object(shape)
lPaddle.speed(0) #set the speed of the animation
lPaddle.shape("square") #set the shape of the object
lPaddle.shapesize(stretch_wid=5 , stretch_len=1) #stretches the shape to meet the size
lPaddle.color("hot pink") #set the color of the shape
lPaddle.penup() #stops the object from drawing lines
lPaddle.goto(-350 , 0) #set the position of the object

#rPaddle
rPaddle = turtle.Turtle()
rPaddle.speed(0)
rPaddle.shape("square")
rPaddle.shapesize(stretch_wid=5 , stretch_len=1) 
rPaddle.color("lavender")
rPaddle.penup()
rPaddle.goto(350 , 0)

#ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("circle") 
ball.color("white") 
ball.penup() 
ball.goto(0 , 0) 
ball.dx=0.3
ball.dy=0.3

# center line
center_line = turtle.Turtle()
center_line.speed(0)
center_line.color("gray")
center_line.penup()
center_line.goto(0, 300)
center_line.setheading(270)

for i in range(20):
    center_line.pendown()
    center_line.forward(15)
    center_line.penup()
    center_line.forward(15)

#score
score1 =0    
last_score1 = 0
last_score2 = 0
score2 =0
winning_score = 5
game_running = True
paused = False
computer_speed = 0.4
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0 , 260)
score.write("player 1 :0        player 2 :0 " , align= "center" , font=("courier", 24, "bold" ))

# controls UI
controls = turtle.Turtle()
controls.speed(0)
controls.color("gray")
controls.penup()
controls.hideturtle()

controls.goto(0, -280)
controls.write(
    "PLAYER 1: W / S        PLAYER 2: ↑ / ↓        P: Pause",
    align="center",
    font=("courier", 12, "normal")
)

#functions
def lPaddle_up():  
    y = lPaddle.ycor()  #get the y coordinate of the lPaddlr
    y +=20 #set the y to increase by 20
    lPaddle.sety(y)  #set the y of the lPaddle to the new y coordinate

def lPaddle_down():
     y = lPaddle.ycor()
     y -=20  #set the y to decrease by 20
     lPaddle.sety(y)  

def rPaddle_up():
    y = rPaddle.ycor()
    y +=20
    rPaddle.sety(y)

def rPaddle_down():
     y = rPaddle.ycor()
     y -=20
     rPaddle.sety(y)

# game functions

def game_over(message):
    global game_running

    game_running = False

    score.clear()
    score.goto(0, 0)
    score.write(message, align="center",
                font=("courier", 30, "normal"))


def restart_game():
    global score1, score2, game_running, paused
    global last_score1, last_score2

    score1 = 0
    score2 = 0
    last_score1 = 0
    last_score2 = 0
    game_running = True
    paused = False

    ball.goto(0, 0)
    ball.dx = 0.3
    ball.dy = 0.3

    lPaddle.goto(-350, 0)
    rPaddle.goto(350, 0)

    score.clear()
    score.goto(0, 260)
    score.write(
        "player 1 :0  player 2 :0",
        align="center",
        font=("courier", 24, "normal")
    )


def pause_game():
    global paused

    paused = not paused   






#keyboard bindings
wind.listen()    #tell the window to expect keyboard input
wind.onkeypress(lPaddle_up, "w")  #when pressing w the finction lPaddle_up is invoked
wind.onkeypress(lPaddle_down, "s")

wind.listen()    
wind.onkeypress(restart_game, "r")
wind.onkeypress(pause_game, "p")
    
    

#main game loop
while True:
    wind.update()

    if not game_running:
        continue

    if paused:
        continue

    # Computer movement
    if ball.ycor() > rPaddle.ycor() and rPaddle.ycor() < 240:
     rPaddle.sety(rPaddle.ycor() + computer_speed)

    elif ball.ycor() < rPaddle.ycor() and rPaddle.ycor() > -240:
     rPaddle.sety(rPaddle.ycor() - computer_speed)
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Player 1 scores
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1

        score.clear()
        score.write(
            "player 1 :{}  player 2 :{}".format(score1, score2),
            align="center",
            font=("courier", 24, "normal")
        )

    # Player 2 scores
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1

        score.clear()
        score.write(
            "player 1 :{}  player 2 :{}".format(score1, score2),
            align="center",
            font=("courier", 24, "normal")
        )

    # Winning check
    if score2 >= winning_score:
        game_over("PLAYER 2 WINS!")

    if score1 >= winning_score:
        game_over("PLAYER 1 WINS!")

    # Right paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
       (ball.ycor() < rPaddle.ycor() + 50 and
        ball.ycor() > rPaddle.ycor() - 50):

        ball.setx(340)
        ball.dx *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1

    # Left paddle collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
       (ball.ycor() < lPaddle.ycor() + 50 and
        ball.ycor() > lPaddle.ycor() - 50):

        ball.setx(-340)
        ball.dx *= -1
        ball.dx *= 1.1
        ball.dy *= 1.1

    