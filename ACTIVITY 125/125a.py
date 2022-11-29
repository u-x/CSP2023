import turtle as trtl
wn = trtl.Screen()

# background
wn.bgcolor("#000000")
trtl.addshape("H:/CSP2023/ACTIVITY 125/keke.gif")

# vars
p1score = 0
p2score = 0

wn.tracer(False)

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
    bgdrawer.pencolor("#ffffff")
    bgdrawer.forward(800)
    bgdrawer.right(90)
    bgdrawer.pencolor("#fefefe")
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

scorefont = ("Bit5x3 Regular", 60, "bold")

# left player score
p1scorewriter = trtl.Turtle()
p1scorewriter.hideturtle()
p1scorewriter.pu()
p1scorewriter.color("white")
p1scorewriter.goto(-20, 220)
p1scorewriter.write("0", align="right", font=scorefont)

# right player score
p2scorewriter = trtl.Turtle()
p2scorewriter.hideturtle()
p2scorewriter.pu()
p2scorewriter.color("white")
p2scorewriter.goto(30, 220)
p2scorewriter.write("0", align="left", font=scorefont)

# left player paddle
p1paddle = trtl.Turtle()
p1paddle.shape("H:/CSP2023/ACTIVITY 125/keke.gif")
p1paddle.penup()
p1paddle.color("#ffffff")
p1paddle.goto(-50, 0)




wn.mainloop()