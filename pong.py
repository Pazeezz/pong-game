#simple pong in python

import turtle
import winsound

wn=turtle.Screen()
wn.title("Pong by @PAZEE")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

frame = turtle.Turtle()
frame.speed(0)
frame.color('white')
frame.penup()
frame.goto(-400, -300)
frame.pendown()
frame.pensize(2)
for side in range(4):
    frame.fd(800)
    frame.lt(90)
    frame.hideturtle()


#score
score_a=0
score_b=0

#paddle A
paddle_a =turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-375,0)

#paddle B
paddle_b =turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(375,0)


#Ball
ball =turtle.Turtle()
ball.speed(10)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx=0.1
ball.dy=-0.1

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  <<<Pong By Pazeez>>>  Player B: 0", align="center", font=("courier", 20
))

#function
def paddle_a_up():
    y=paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y=y+20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")    
wn.onkeypress(paddle_a_down, "s")    
wn.onkeypress(paddle_b_up, "Up")    
wn.onkeypress(paddle_b_down, "Down")

#Main game loop
while True:
    wn.update()
    


    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    
    #border cheking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy=ball.dy*-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC) 

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy=ball.dy*-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        

    elif ball.xcor() > 350:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        score_a +=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  <<<Pong By Pazeez>>>  Player B: {}".format(score_a, score_b), align="center", font=("courier", 20, "italic"))
    
    elif ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx=ball.dx*-1
        score_b +=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {}  <<<Pong By Pazeez>>>  Player B: {}".format(score_a, score_b), align="center", font=("courier", 20, "italic"))

#pabble and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
   
    
