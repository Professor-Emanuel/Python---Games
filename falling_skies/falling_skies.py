import turtle
import random
import os
import winsound

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Skies by E.K.")
wn.bgcolor("black")
wn.bgpic("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\\background.gif")
wn.setup(width=1200, height=800)
wn.tracer(15)


wn.register_shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_left.gif")
wn.register_shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_right.gif")
wn.register_shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_nut.gif")
wn.register_shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_hunter.gif")


#add the player
player = turtle.Turtle()
player.speed(0)
player.shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_left.gif")
player.color("white")
player.penup() #it has to be before goto(), so it will not draw any lines
player.goto(0, -250)
player.direction = "stop"

#create a list of good guys
good_guys = []

#add the good_guys
for _ in range(20):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_nut.gif")
    good_guy.color("red")
    good_guy.penup()
    x = random.randint(-580, 580)
    y = random.randint(300, 400)
    good_guy.goto(x, y)
    good_guy.speed = random.randint(1, 4)
    good_guys.append(good_guy)

#create a list of bad guys
bad_guys = []
#add the bad guys
for _ in range(20):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_hunter.gif")
    bad_guy.color("yellow")
    bad_guy.penup()
    x = random.randint(-580, 580)
    y = random.randint(300, 400)
    bad_guy.goto(x, y)
    bad_guy.speed = random.randint(1, 4)
    bad_guys.append(bad_guy)

#Make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, -380)
font =  ("Courier", 24, "normal")
pen.write("Score: {} Lives: {}".format(score, lives), align="center", font = font)

#functions
def go_left():
    player.direction = "left"
    player.shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_left.gif")

def go_right():
    player.direction = "right"
    player.shape("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_right.gif")

def go_up():
    player.direction = "up"

def go_down():
    player.direction = "down"

wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")

#main game loop
while True:
    #update the screen
    wn.update()
    #move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)
        if x < -550:
            player.direction = "stop"
        


    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)
        if x > 550:
            player.direction = "stop"

    if player.direction == "up":
        y = player.ycor()
        y += 3
        player.sety(y)
        if y > 250:
            player.direction = "stop"

    if player.direction == "down":
        y = player.ycor()
        y -= 3
        player.sety(y)
        if y < -250:
            player.direction = "stop"

    #move the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)
        #analogous:
        #good_guy.sety(good_guy.ycor() - 3)

        #check if off the screen
        if y < - 300:
            x = random.randint(-580, 580)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
        
        #check for a collision with the player
        if good_guy.distance(player) < 40:
            winsound.PlaySound("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_nut_up.wav", winsound.SND_ASYNC)
            x = random.randint(-580, 580)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font = font)
        if lives == 0:
            good_guy.hideturtle()
            print("Game Over")
            


    #move the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)
        #analogous:
        #bad_guy.sety(badd_guy.ycor() - 3)

        #check if off the screen
        if y < - 300:
            x = random.randint(-580, 580)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
        #check for a collision with the player
        if bad_guy.distance(player) < 40:
            winsound.PlaySound("D:\OneDrive - e-uvt.ro\Lessons\Python\\falling_skies\deer_hunter_down.wav", winsound.SND_ASYNC)
            x = random.randint(-580, 580)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {} Lives: {}".format(score, lives), align="center", font = font)
        if lives == 0:
            player.setx(1500)
            player.sety(1500)
            bad_guy.hideturtle()
            print("Game Over")
           
            


wn.mainloop()
