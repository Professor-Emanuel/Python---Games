    #check for a wall collision
        if ball.xcor() > 300:
            ball.dx *= -1
        if ball.xcor() < -300:
            ball.dx *= -1
        #check for a  bounce
        if ball.ycor() < -300:
            ball.dy *= -1