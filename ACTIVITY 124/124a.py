# import
import turtle as trtl
import random

# variables

wallthiccness = 5
wallcolor = "blue"
pathwidth = 15
walllength = pathwidth
sides = 25
dooropeninglength = pathwidth * 2
restwalllength = 0
doorStartLocation = 10
barrierstartloc = 40

# turtle

maze_drawer = trtl.Turtle()
maze_drawer.speed(0)
maze_drawer.pencolor(wallcolor)
maze_drawer.pensize(wallthiccness)
keys = ["Up", "Down", "Left", "Right"]

mazerunner = trtl.Turtle(shape="arrow")
mazerunner.penup()
mazerunner.goto(-20, 0)
mazerunner.pendown()
mazerunner.fillcolor("green")
mazerunner.pencolor("green")


# funcs
def draw_door(pos):
    maze_drawer.forward(pos)
    # door
    maze_drawer.pu()
    maze_drawer.forward(dooropeninglength)
    maze_drawer.pd()

def draw_barrier(pos):
    maze_drawer.forward(pos)
    maze_drawer.left(90)
    maze_drawer.forward(pathwidth*2)
    maze_drawer.backward(pathwidth*2)
    maze_drawer.right(90)

def draw_restofwall(pos):
    maze_drawer.forward(pos)

def moverunner(key):
    if key == "Left":
        mazerunner.setheading(180)
    elif key == "Right":
        mazerunner.setheading(0)
    elif key == "Up":
        mazerunner.setheading(90)
    elif key == "Down":
        mazerunner.setheading(270)
    mazerunner.forward(5)
        

for side in range(0, sides, 1):
    walllength += pathwidth
    if side <= 5:
        maze_drawer.left(90)
        maze_drawer.forward(walllength)
    else:
        randdoor = random.randint((pathwidth * 2), (walllength - (pathwidth * 2)))
        randbarrier = random.randint((pathwidth * 2), (walllength - (pathwidth * 2)))

        while abs(randdoor - randbarrier) < pathwidth:
            randdoor = random.randint((pathwidth * 2), (walllength - (pathwidth * 2)))
        
        maze_drawer.left(90)
        if (randdoor < randbarrier):
            draw_door(randdoor)
            draw_barrier(randbarrier - dooropeninglength - randdoor)
            draw_restofwall(walllength - randbarrier)

        else:
            draw_barrier(randbarrier)
            draw_door(randdoor - randbarrier)
            draw_restofwall(walllength - dooropeninglength - randdoor)

    # walllength -= pathwidth
maze_drawer.hideturtle()
wn = trtl.Screen()

# keypresses
for key in keys:
    wn.onkeypress(lambda key=key: moverunner(key), key)
# events
wn.listen()
wn.mainloop()