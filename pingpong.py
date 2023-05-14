
import turtle
import os


windows= turtle.Screen()
windows.title("Ping Pong Ball Game")
windows.bgcolor("black")
windows.setup(width=1000,height=800)
windows.tracer(0)
PlayerA=0
PlayerB=0

border = turtle.Turtle()
border.color('white')
border.penup()
border.goto(400,0)
border.pensize(2)
border.hideturtle()
border.pendown()
border.left(90)
border.forward(300)
border.left(90)
border.forward(800)
border.left(90)
border.forward(600)
border.left(90)
border.forward(800)
border.left(90)
border.forward(300)


pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.goto(0,330)
pen.hideturtle()
pen.write("Player A:0  Player B:0",align="center",font=("Courier",20,"normal"))

p2=turtle.Turtle()
p2.speed(0)
p2.penup()
p2.color("white")
p2.goto(0,360)
p2.hideturtle()
p2.write("GAME",align="center",font=("Courier",20,"normal"))

left_paddle= turtle.Turtle()
left_paddle.speed(0)
left_paddle.color("blue")
left_paddle.penup()
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.goto(-350,0)

right_paddle= turtle.Turtle()
right_paddle.speed(0)
right_paddle.color("red")
right_paddle.penup()
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.goto(350,0)

ball= turtle.Turtle()
ball.speed(0)
ball.color("green")
ball.penup()
ball.shape("circle")
ball.goto(0,0)
ball.dx=5
ball.dy=-5

def left_paddle_up():
    y= left_paddle.ycor()
    y+=20
    left_paddle.sety(y)
def left_paddle_down():
    y= left_paddle.ycor()
    y-=20
    left_paddle.sety(y)

def right_paddle_up():
    y= right_paddle.ycor()
    y+=20
    right_paddle.sety(y)
def right_paddle_down():
    y= right_paddle.ycor()
    y-=20
    right_paddle.sety(y)


windows.listen()
windows.onkeypress(left_paddle_up,"w")
windows.onkeypress(left_paddle_down,"s")
windows.onkeypress(right_paddle_up,"Up")
windows.onkeypress(right_paddle_down,"Down")





while True:
    windows.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        os.system("afplay Bounce.wav&")
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        os.system("afplay Bounce.wav&")
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        os.system("afplay Lose.wav&")
        PlayerA+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(PlayerA,PlayerB),align="center",font=("Courier",20,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        os.system("afplay Lose.wav&")
        PlayerB+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(PlayerA,PlayerB),align="center",font=("Courier",20,"normal"))
    
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<right_paddle.ycor()+45 and ball.ycor()>right_paddle.ycor()-45):
        ball.setx(340)
        ball.dx*=-1
        os.system("afplay Bounce.wav&")
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<left_paddle.ycor()+45 and ball.ycor()>left_paddle.ycor()-45):
        ball.setx(-340)
        ball.dx*=-1
        os.system("afplay Bounce.wav&")
#Bonus
    if (PlayerA or PlayerB)>1:
        right_paddle.shapesize(stretch_wid=6,stretch_len=1)
        left_paddle.shapesize(stretch_wid=6,stretch_len=1)
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<right_paddle.ycor()+55 and ball.ycor()>right_paddle.ycor()-55):
        ball.setx(340)
        ball.dx*=-1
        os.system("afplay Bounce.wav&")
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<left_paddle.ycor()+55 and ball.ycor()>left_paddle.ycor()-55):
        ball.setx(-340)
        ball.dx*=-1
        os.system("afplay Bounce.wav&")
    



