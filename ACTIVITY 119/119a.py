import turtle

stamp = turtle.Turtle()
stamp.pu()
stamp.shape("square")
stamp.shapesize(1)
stamp.speed(0)

wn = turtle.Screen()
wn.setup(width=1000, height=1000)
wn.title("i did your mother last night")
wn.bgcolor("LightSkyBlue")

yax = 160

# hat start
stamp.color("#ff0000")
stamp.goto(60, yax)
yax -= 20
stamp.setheading(180)
for step in range(6):
    stamp.stamp()
    stamp.forward(20)
stamp.goto(120, yax)
yax -= 20
for step in range(10):
    stamp.stamp()
    stamp.forward(20)

# hat end, head start
stamp.color("#fac090")

stamp.goto(120, yax)
yax -= 20

for step in range(9):
    if step == 1:
        # face
        stamp.color('#000000')
    elif step > 5:
        # hair
        stamp.color('#974807')
    else:
        # skin
        stamp.color("#fac090")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(160, yax)
yax -= 20

for step in range(12):
    if step == 3:
        # face
        stamp.color('#000000')
    elif step == 9 or step == 11:
        # hair
        stamp.color('#974807')
    else:
        # skin
        stamp.color("#fac090")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(180, yax)
yax -= 20

for step in range(13):
    if step == 3:
        # face
        stamp.color('#000000')
    elif step > 8 and step != 11:
        # hair
        stamp.color('#974807')
    else:
        # skin
        stamp.color("#fac090")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(160, yax)
yax -= 20

for step in range(12):
    if step < 4:
        # face
        stamp.color('#000000')
    elif step > 9:
        # hair
        stamp.color('#974807')
    else:
        # skin
        stamp.color("#fac090")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(140, yax)
yax -= 20
stamp.color("#fac090")

for step in range(9):
    stamp.forward(20)
    stamp.stamp()

# head end, lower body start


stamp.goto(80, yax)
yax -= 20

for step in range(7):
    if step == 4:
        # overalls start here
        stamp.color("#0474c4")
    else:
        # shirt
        stamp.color("#ff0000")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(120, yax)
yax -= 20

for step in range(10):
    if step == 3 or step == 6:
        # overalls
        stamp.color("#0474c4")
    else:
        # shirt
        stamp.color("#ff0000")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(140, yax)
yax -= 20

for step in range(12):
    if step >= 4 and step <= 7:
        # overalls
        stamp.color("#0474c4")
    else:
        # shirt
        stamp.color("#ff0000")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(140, yax)
yax -= 20

for step in range(12):
    if step < 2 or step > 9:
        # hands
        stamp.color("#fac090")
    elif step == 4 or step == 7:
        # buttons
        stamp.color("#ffff00")
    elif step >= 3 and step <= 8:
        # overalls
        stamp.color("#0474c4")
    else:
        # shirt
        stamp.color("#ff0000")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(140, yax)
yax -= 20

for step in range(12):
    if step >= 3 and step <= 8:
        # overalls
        stamp.color("#0474c4")
    else:
        # hands
        stamp.color("#fac090")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(140, yax)
yax -= 20

for step in range(12):
    if step <= 1 or step >= 10:
        # hands
        stamp.color("#fac090")
    else:
        # overalls
        stamp.color("#0474c4")
    stamp.forward(20)
    stamp.stamp()

stamp.goto(100, yax)
yax -= 20
stamp.color("#0474c4")

for step in range(8):
    if step == 3 or step == 4:
        stamp.forward(20)
    else:
        stamp.forward(20)
        stamp.stamp()

# WHAT ARE THOSE (shoes)
stamp.goto(120, yax)
yax -= 20
stamp.color("#974807")

for step in range(10):
    if step >= 3 and step <= 6:
        stamp.forward(20)
    else:
        stamp.forward(20)
        stamp.stamp()

stamp.goto(140, yax)
yax -= 40
stamp.color("#974807")

for step in range(12):
    if step >= 4 and step <= 7:
        stamp.forward(20)
    else:
        stamp.forward(20)
        stamp.stamp()

# ground
stamp.goto(1500, yax)
yax -= 60
wn.addshape("groundblock.gif")
stamp.shape("groundblock.gif")

for step in range(500):
    stamp.forward(60)
    stamp.stamp()
    if step % 75 == 0 and step != 0:
        stamp.goto(1500, yax)
        yax -= 60

wn.addshape("questionblock.gif")
stamp.shape("questionblock.gif")
stamp.goto(20, 380)

stamp.stamp()

stamp.shape("classic")
stamp.goto(-500, 600)
stamp.pd()
stamp.pencolor('#ffff00')
stamp.fillcolor("#ffff00")
stamp.begin_fill()
stamp.pensize(5)
stamp.turtlesize(1)
stamp.circle(100)
stamp.end_fill()

head = 360

for angles in range(11):
    stamp.pu()
    stamp.goto(-500, 500)
    stamp.setheading(head)
    stamp.pd()
    stamp.forward(125)
    head -= 9

wn.mainloop()