# space invaders - part 1
# set up the screen
# Python 3.6 on Windows
import turtle
import os
import math
import random
import winsound

# set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\space_invaders_background.gif")

#register the shapes
turtle.register_shape("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\space_invader.gif")
turtle.register_shape("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\space_player.gif")
#draw a border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score = 0
#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("White")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create the player turtle

player = turtle.Turtle()
player.color("blue")
player.shape("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\space_player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#choose a number of enemies
number_of_enemies = 5

#create an empty list of enemies
enemies = [] # empty list

#add enemies to the list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle()) #instead of creating we are appending enemies to the list


#create the enemy
for enemy in enemies:
    enemy.color("White")
    enemy.shape("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\space_invader.gif")
    enemy.penup() # so the enemy will not draw anything
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# create the player's bullet

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup() # so the bullet will not draw anything
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move the player left and right

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #declare bulletstate as a global if it needs changed
    global bulletstate #use of keyword "global" is required because we might wanna
                        # change this variable, any changes in this function will be 
                        # reflected up there where we created the variable, also.
    if bulletstate == "ready":
        winsound.PlaySound("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\laser.wav", winsound.SND_ASYNC) #windows
        # os.system("aplay sound2.wav&") for Linux
        # os.system("afplay sound2.wav&") for Mac
        bulletstate = "fire"
        #move the bullet to just about the player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

# create keybord binding
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#main game loop
while True:
    for enemy in enemies:
        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies: 
                #added these loop so each enemy goes down, not just one
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                #added these loop so each enemy goes down, not just one
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change enemy direction
            enemyspeed *= -1

        #check for collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\explosion.wav", winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #update score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        #check for collision between the player and enemy
        if isCollision(player, enemy):
            winsound.PlaySound("D:\OneDrive - e-uvt.ro\Lessons\Python\space_invaders\explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

        #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


delay = input("Press enter to finish.")
