import turtle as trtl

painter = trtl.Turtle()

painter.turtlesize(3)
painter.pencolor('green')
painter.pensize(3)

for i in range(4):
    painter.forward(100)
    painter.right(90)
    painter.circle(20)
 
wn = trtl.Screen()
wn.mainloop()