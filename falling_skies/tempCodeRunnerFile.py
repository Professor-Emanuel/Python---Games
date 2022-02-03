    y = good_guy.ycor()
        y -= 3
        good_guy.sety(y)
        #analogous:
        #good_guy.sety(good_guy.ycor() - 3)

        #check if off the screen
        if y < - 300:
            x = random.randint(-580, 580)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
        
        #check for a collision with the player
        if good_guy.distance(player) < 20:
            x = random.randint(-580, 580)
            y = random.randint(300, 400)
            good_guy.goto(x, y)