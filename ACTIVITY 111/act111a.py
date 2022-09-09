import turtle as trtl

painter = trtl.Turtle()

# mods
painter.turtlesize(3)
painter.pencolor('cornflower blue')
painter.color('cornflower blue')
painter.pensize(3)

for i in range(4):
    painter.forward(100)
    painter.right(90)
    painter.circle(20)

painter.left(90)
for i in range(4):
    painter.forward(100)
    painter.left(90)
    painter.circle(20)
 
wn = trtl.Screen()
wn.mainloop()