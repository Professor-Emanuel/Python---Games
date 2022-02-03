#Python 3.6

import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#set up the screen
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Snake Game by E.K")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the animation on the screen, screen updates, so the modules can go as fast as possible

# create snake head
head = turtle.Turtle() #create the turtle, then give it some properties like:
head.speed(0) #animation speed of the turtle module, not the speen of moving on the screen
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0) #this positions it in the center of the screen;
               #actually turtule module always start in the center of the screen
               #but it is a good practice to set things the way you want it
head.direction = "stop"

# create the snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

#pen
pen = turtle.Turtle()
pen.speed(0) #this is the animation speed
pen.shape("square") #shape does not matter because we are not going to see it
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))
#create the functions that will make the snake move
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

segments = [] # create an empty list, the snake has just the had when the game starts
                #when the snake touches the food, add a segment to it

#create the functions that will make the snake change drections
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#create keybord bindings

wn.listen()
wn.onkeypress(go_up,"Up") # or instead of w, use Up
wn.onkeypress(go_down, "Down") #or instead of s, use Down
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

#main game loop
while True:
    wn.update()

    #check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000, 1000) # no way to delete the modules in 
            #python turtle, so we move them far away of the visible screen
        #clear the segments list
        segments.clear()    #pyhton 3.3+
        #segments = [] in python 2.
        
        # reset te score
        score = 0

        # reset the delay
        delay = 0.1
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for a collision with the food
    if head.distance(food) < 20: #the basic turtle shape is 20pixels x 20pixels
    #move the food to a randome spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)  #animation speed
        new_segment.shape("square")
        new_segment.penup()
        new_segment.color("black")
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001

        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    #move the end segment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()#clear the segents list

            # reset te score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay) # we have to setup this delay, so we can see the
                        #snake moving, otherwise the turtle moves of the screen
                        # so fast that we do not see it.



wn.mainloop()