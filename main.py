import turtle
import random

screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")  
screen.bgpic("background.gif") 
screen.tracer(0)

paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("lightblue") 
paddle1.shapesize(stretch_wid=6, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("lightcoral") 
paddle2.shapesize(stretch_wid=6, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")  
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

score1 = 0
score2 = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

def paddle1_up():
    y = paddle1.ycor()
    if y < 250:
        y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    if y > -240:
        y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    if y < 250:
        y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    if y > -240:
        y -= 20
    paddle2.sety(y)

screen.listen()
screen.onkeypress(paddle1_up, "w")
screen.onkeypress(paddle1_down, "s")
screen.onkeypress(paddle2_up, "Up")
screen.onkeypress(paddle2_down, "Down")

def update_scoreboard():
    scoreboard.clear()
    scoreboard.write(f"Player 1: {score1}  Player 2: {score2}", align="center", font=("Courier", 24, "normal"))

def check_win():
    if score1 >= 5:
        scoreboard.clear()
        scoreboard.write("Player 1 Wins!", align="center", font=("Courier", 36, "normal"))
        return True
    elif score2 >= 5:
        scoreboard.clear()
        scoreboard.write("Player 2 Wins!", align="center", font=("Courier", 36, "normal"))
        return True
    return False

while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score1 += 1
        update_scoreboard()
        if check_win():
            break
        ball.goto(0, 0)
        ball.dx = -0.2
        ball.dy = random.uniform(-0.2, 0.2)

    if ball.xcor() < -390:
        score2 += 1
        update_scoreboard()
        if check_win():
            break
        ball.goto(0, 0)
        ball.dx = 0.2
        ball.dy = random.uniform(-0.2, 0.2)

    if (ball.dx > 0 and 340 < ball.xcor() < 350) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0 and -350 < ball.xcor() < -340) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1