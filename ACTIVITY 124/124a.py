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

# funcs

def draw_door(loc):
    # wall b4 door
    maze_drawer.forward(loc)
    # door
    maze_drawer.pu()
    maze_drawer.forward(dooropeninglength)
    maze_drawer.pd()

def draw_barrier(loc):
    # wall b4 barrier
    maze_drawer.forward(loc - dooropeninglength - randdoor)

    # barrier
    maze_drawer.left(90)
    maze_drawer.forward(pathwidth*2)
    maze_drawer.backward(pathwidth*2)
    maze_drawer.right(90)

# turtle

maze_drawer = trtl.Turtle()
maze_drawer.speed(0)
maze_drawer.pencolor(wallcolor)
maze_drawer.pensize(wallthiccness)

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

            # wall b4 barrier
            maze_drawer.forward(randbarrier - dooropeninglength - randdoor)

            # barrier
            maze_drawer.left(90)
            maze_drawer.forward(pathwidth*2)
            maze_drawer.backward(pathwidth*2)
            maze_drawer.right(90)

            # rest of wall
            restwalllength = (walllength - randbarrier)
            maze_drawer.forward(restwalllength)

        else:
            # wall b4 barrier
            maze_drawer.forward(randbarrier)

            # barrier
            maze_drawer.left(90)
            maze_drawer.forward(pathwidth*2)
            maze_drawer.backward(pathwidth*2)
            maze_drawer.right(90)

            # wall 2 door
            maze_drawer.forward(randdoor - randbarrier)
            maze_drawer.pu()
            maze_drawer.forward(dooropeninglength)
            maze_drawer.pd()

            # rest of wall
            restwalllength = (walllength - dooropeninglength - randdoor)
            maze_drawer.forward(restwalllength)

    # walllength -= pathwidth
maze_drawer.hideturtle()

# funcs

# events
wn = trtl.Screen()
wn.mainloop()