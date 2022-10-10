import turtle

stamp = turtle.Turtle()
stamp.pu()
stamp.shape("square")
stamp.shapesize(1)

# hat start
stamp.color("#ff0000")
stamp.goto(60, 160)
stamp.setheading(180)
for step in range(6):
    stamp.stamp()
    stamp.forward(20)
stamp.goto(120, 140)
for step in range(10):
    stamp.stamp()
    stamp.forward(20)

# hat end, head start
stamp.color("#fac090")

stamp.goto(120, 120)

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

stamp.goto(160, 100)

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

stamp.goto(180, 80)

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

stamp.goto(160, 60)

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

stamp.goto(140, 40)
stamp.color("#fac090")

for step in range(9):
    stamp.forward(20)
    stamp.stamp()

# head end, lower body start





wn = turtle.Screen()
wn.mainloop()