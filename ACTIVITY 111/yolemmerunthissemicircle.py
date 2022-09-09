import turtle as trtl

paint = trtl.Turtle()

# mods
paint.turtlesize(0.001)
paint.pencolor('navy')
paint.color('navy')
paint.pensize(10)

paint.begin_fill()
paint.fillcolor('navy')
paint.left(90)
paint.circle(50, 180)
paint.left(90)
paint.forward(100)
paint.left(360)
paint.left(180)
paint.end_fill()

wn = trtl.Screen()
wn.mainloop()