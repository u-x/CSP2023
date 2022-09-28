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

col = int(input("Which column should be shaded? (pick a number 1 through 7) "))

for j in range(8):
    for i in range(7):
        if i == col - 1:
            painter.color("red")
        else:
            painter.color("blue")
        painter.stamp()
        x = x + 100
        if i == 6:
            x = -300
            y = y - 100
        painter.goto(x,y)

wn = turtle.Screen()
wn.mainloop()