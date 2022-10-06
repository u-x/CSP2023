#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# init direction var
direction = 90

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  t.pu()
  t.color(turtle_colors.pop())

# turtle spawn point
startx = 0
starty = 0

# continue pattern
for t in my_turtles:
  t.goto(startx, starty)
  t.setheading(direction)
  t.pd()
  t.right(45)     
  t.forward(50)
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()

wn = trtl.Screen()
wn.mainloop()