import turtle as trtl
wn = trtl.Screen()

# background
wn.bgcolor("#000000")

# vars
p1score = 0
p2score = 0

# borders
bgdrawer = trtl.Turtle(shape="square")
bgdrawer.turtlesize(0.25)
bgdrawer.pencolor("#ffffff")
bgdrawer.fillcolor("#ffffff")
bgdrawer.penup()
bgdrawer.goto(-400, 300)
bgdrawer.pensize(10)
bgdrawer.pd()
for i in range(2):
    bgdrawer.forward(800)
    bgdrawer.right(90)
    bgdrawer.forward(600)
    bgdrawer.right(90)
bgdrawer.pu()
bgdrawer.goto(0, 300)
bgdrawer.pencolor("#fffffe")
bgdrawer.setheading(270)
for i in range(300):
    if i % 10 == 0:
        bgdrawer.stamp()
        bgdrawer.forward(2)
    else:
        bgdrawer.forward(2)

scorefont = ("Pong Score", 20, "bold")

# left player score
p1scorewriter = trtl.Turtle()
p1scorewriter.hideturtle()
p1scorewriter.pu()
p1scorewriter.color("white")
p1scorewriter.goto(-20, 250)
p1scorewriter.write("0", align="center", font=scorefont)


wn.mainloop()