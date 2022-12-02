import turtle as trtl
import random
import time
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
# p1paddle.shape("H:\\CSP2023\\ACTIVITY 125\\keke.gif")
p1paddle.shape("square")
p1paddle.shapesize(stretch_len=6)
p1paddle.setheading(90)
p1paddle.penup()
p1paddle.color("#ffffff")
p1paddle.goto(-365, 0)

# right player paddle
p2paddle = trtl.Turtle()
# p2paddle.shape("H:\\CSP2023\\ACTIVITY 125\\keke.gif")
p2paddle.shape("square")
p2paddle.shapesize(stretch_len=6)
p2paddle.setheading(90)
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
    global ballinplay, p1score, p2score
    pball.goto(0, 0)
    angled = False
    angle = 0
    while angled == False:
        if angle >= 65 and angle <= 115:
            angle = random.randint(0, 360)
        elif angle < 65:
            angle = random.randint(0, 360)
        elif angle >= 255 and angle <= 295:
            angle = random.randint(0, 360)
        else:
            angled = True
    if (angled == True):
        pball.setheading(angle)
        time.sleep(1)
        ballinplay = True
        while ballinplay == True:
            bounce = False
            pball.forward(3)
            cury = pball.ycor()
            if (cury <= -297):
                anglern = pball.heading()
                bruhangle = anglern
                pball.setheading(360-bruhangle)
            elif cury >= 297:
                anglern = pball.heading()
                bruhangle = anglern
                pball.setheading(360-bruhangle)
            if (pball.xcor() >= 397):
                p1score += 1
                p1scorewriter.clear()
                p1scorewriter.write(str(p1score), align="right", font=scorefont)
                ballinplay = False
                play_ball()
            elif (pball.xcor() <= -397):
                p2score += 1
                p2scorewriter.clear()
                p2scorewriter.write(str(p2score), align="left", font=scorefont)
                ballinplay = False
                play_ball()
            if (pball.distance(p1paddle) < 60):
                print(bounce)
                if bounce == False:
                    bounce = True
                    anglern = pball.heading()
                    bruhangle = anglern
                    pball.setheading((360-bruhangle)+180)
            elif (pball.distance(p2paddle) < 60):
                if bounce == False:
                    bounce = True
                    anglern = pball.heading()
                    bruhangle = anglern
                    pball.setheading(180-bruhangle)
            else:
                bounce = False

def leftup():
    global p1paddle, p2paddle
    p1paddle.forward(10)

def leftdown():
    global p1paddle, p2paddle
    p1paddle.backward(10)

def rightup():
    global p1paddle, p2paddle
    p2paddle.forward(10)

def rightdown():
    global p1paddle, p2paddle
    p2paddle.backward(10)

wn.onkeypress(leftup, "w")
wn.onkeypress(leftdown, "s")
wn.onkeypress(rightup, "Up")
wn.onkeypress(rightdown, "Down")
wn.listen()
play_ball()

wn.mainloop()