# a121_catch_a_turtle.py
#-----import statements-----

import turtle
import random
import leaderboard as lb

#-----game configuration----

spot_color = "pink"
spritesize = 2
spriteshape = "circle"
score = 0

lbfile = "122lb.txt"
pname = input("What is your name? ")

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
fontsettings = ("Arial", 20, "normal")

counter =  turtle.Turtle()
counter.pu()
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
    t.hideturtle()
    newx = random.randint(-200, 200)
    newy = random.randint(-200, 200)
    t.goto(newx, newy)
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
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=fontsettings)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def manage_leaderboard():

  global score
  global t

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(lbfile)
  leader_scores_list = lb.get_scores(lbfile)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(lbfile, leader_names_list, leader_scores_list, pname, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, t, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, t, score)

#-----events----------------
t.onclick(spot_clicked)
wn = turtle.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()