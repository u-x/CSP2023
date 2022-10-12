import turtle

stamp = turtle.Turtle()
stamp.pu()
stamp.shape("square")
stamp.shapesize(1)
stamp.speed(0)

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

wn = turtle.Screen()
wn.mainloop()