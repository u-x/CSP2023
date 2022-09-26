import turtle

painter = turtle.Turtle()

x = -300
y = 300

painter.penup()
painter.goto(x,y)
painter.shape("circle")
painter.hideturtle()
painter.shapesize(2)
painter.speed(0)

inc = 0

for j in range(8):
    for i in range(inc * -1, inc + 1, 1):
        print(i)
        if i == 0:
            painter.color("red")
        else:
            painter.color("blue")
        print(x)
        painter.stamp()
        x = x + 100
        if i == inc:
            x = -400 + (100 * (inc * -1))
            y = y - 100
            inc = inc + 1
        painter.goto(x,y)

wn = turtle.Screen()
wn.mainloop()