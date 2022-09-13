import turtle as trtl

pen = trtl.Turtle()

# mods
pen.turtlesize(0.001)
pen.pencolor('navy')
pen.color('navy')
pen.pensize(10)

pen.penup()
pen.goto(0, 200)
pen.pendown()

pen.right(60)
pen.forward(200)
pen.right(120)
pen.forward(200)
pen.right(120)
pen.forward(200)

pen.penup()
pen.goto(-75, 20)
pen.pendown()
pen.right(150)
pen.forward(150)
pen.left(90)
pen.forward(150)
pen.left(90)
pen.forward(150)

pen.penup()
pen.goto(-25, -130)
pen.pendown()
pen.forward(75)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(75)

pen.penup()
pen.goto(-60, -30)
pen.pendown()
pen.circle(15)

pen.penup()
pen.goto(30, -30)
pen.pendown()
pen.circle(15)



wn = trtl.Screen()
wn.mainloop()