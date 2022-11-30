import turtle as trtl
import random
wn = trtl.Screen()

# background
wn.bgcolor("#000000")
trtl.addshape("H:\\CSP2023\\ACTIVITY 125\\keke.gif")

# vars
p1score = 0
p2score = 0
ballinplay = False

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
wn.tracer(True)

# left player paddle
p1paddle = trtl.Turtle()
p1paddle.shape("H:\\CSP2023\\ACTIVITY 125\\keke.gif")
p1paddle.penup()
p1paddle.color("#ffffff")
p1paddle.goto(-365, 0)

# left player paddle
p2paddle = trtl.Turtle()
p2paddle.shape("H:\\CSP2023\\ACTIVITY 125\\keke.gif")
p2paddle.penup()
p2paddle.color("#ffffff")
p2paddle.goto(365, 0)

pball = trtl.Turtle()
pball.shape("square")
pball.color("white")
pball.pu()
pball.turtlesize(1)
pball.speed("fastest")

def play_ball():
    global ballinplay
    pball.goto(0, 0)
    angled = False
    angle = 0
    while angled == False:
        if angle >= 0 and angle <= 45:
            angle = random.randint(0, 360)
        elif angle >= 315:
            angle = random.randint(0, 360)
        elif angle >= 135 and angle <= 225:
            angle = random.randint(0, 360)
        else:
            angled = True
    print(angle)
    if (angled == True):
        pball.setheading(angle)
        ballinplay = True
        while ballinplay == True:
            pball.forward(3)
            # if (pball.ycor() <= -290 or pball.ycor >= 290):
            #     anglern = pball.heading()
            #     if (anglern > 180):
            #         bruhangle = anglern-90
            #         if pball.ycor > 0:
            #             pball.setheading(270-)

play_ball()

wn.mainloop()