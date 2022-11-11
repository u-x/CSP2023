# import
import turtle as trtl

# variables

wallthiccness = 5
wallcolor = "blue"
pathwidth = 15
walllength = pathwidth
sides = 25
doorStartLocation = 10
dooropeninglength = pathwidth * 2

# turtle

maze_drawer = trtl.Turtle()
maze_drawer.speed(0)
maze_drawer.pencolor(wallcolor)
maze_drawer.hideturtle()
maze_drawer.pensize(wallthiccness)

for side in range(0, sides, 1):
    maze_drawer.left(90)
    maze_drawer.forward(doorStartLocation)
    maze_drawer.pu()
    maze_drawer.forward(dooropeninglength)
    maze_drawer.pd()
    walllength = (walllength + pathwidth) - doorStartLocation - dooropeninglength
    maze_drawer.forward(walllength)
    # walllength -= pathwidth

# funcs

# events
wn = trtl.Screen()
wn.mainloop()