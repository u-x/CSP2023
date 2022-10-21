# a121_catch_a_turtle.py
#-----import statements-----

from tracemalloc import start
import turtle
import random

#-----game configuration----

spot_color = "pink"
spritesize = 2
spriteshape = "circle"
score = 0

#-----initialize turtle-----

t = turtle.Turtle()

t.shape(spriteshape)
t.fillcolor(spot_color)
t.shapesize(spritesize)
t.penup()

scorewriter = turtle.Turtle()
scorewriter.pu()
scorewriter.hideturtle()
scorewriter.goto(0, 375)
scorewriter.color("#ffffff")
fontsettings = ("Arial", 20, "normal")

counter =  turtle.Turtle()
counter.pu()
counter.color("#ffffff")
counter.hideturtle()
counter.goto(0, -400)
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----game functions--------

def spot_clicked(x, y):
    global timer_up
    if (timer_up == True):
        t.hideturtle()
    else:
        update_score()
        change_position()

def change_position():
    t.shapesize(0.01)
    t.hideturtle()
    newx = random.randint(-200, 200)
    newy = random.randint(-200, 200)
    t.goto(newx, newy)
    t.shapesize(random.randint(1, 4))
    t.showturtle()

def update_score():
    global score
    score += 1
    scorewriter.clear()
    scorewriter.write(score, font=fontsettings)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=fontsettings)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=fontsettings)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
wn = turtle.Screen()
wn.bgcolor("#000000")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
t.onclick(spot_clicked)