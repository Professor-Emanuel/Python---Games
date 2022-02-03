import turtle
import random
import os

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing ball simulator by E.K.")
wn.tracer(2)

balls = []
for _ in range(5):
    balls.append(turtle.Turtle())

colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
my_sizes = [0.5, 1, 1.5, 2, 2.5, 3]
for ball in balls:
    ball.shape("circle")
    ball.color(random.choice(colors))
    ball.shapesize(random.choice(my_sizes))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        if ball.ycor() < -290:
            ball.sety(-290)
        if ball.ycor() > 290:
            ball.sety(290)
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        #check for a wall collision
        if ball.xcor() > 600:
            ball.dx *= -1
            ball.da *= -1
        if ball.xcor() < -600:
            ball.dx *= -1
            ball.da *= -1
        #check for a  bounce
        if ball.ycor() < -300:
            ball.dy *= -1
            ball.da *= -1

wn.mainloop()