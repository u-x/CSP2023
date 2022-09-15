import turtle

from numpy import square

pen = turtle.Turtle()

pen.pensize(5)

print("Let's make a cool little emblem, eh?")
print()

bkg = input('What color should the background be? ')
print()
turtle.bgcolor(bkg)
print("Cool! Let's make our first mark on there!")

def keepshape():
    firstshape = input("What shape should we put on? (square, triangle, circle, done) ")
    if firstshape.lower() == "done":
        print("Yay! Look at your amazing shape!")
    else:
        firstcolor = input("What color should we make this " + firstshape + "? ")
        shapesize = int(input("How big should this " + firstshape + " be? "))

        if firstshape.lower() == "square":
            
            pen.penup()
            pen.goto((shapesize / -2), (shapesize / -2))
            pen.pencolor(firstcolor)
            pen.fillcolor(firstcolor)
            pen.begin_fill()
            pen.pendown()
            for i in range(4):
                pen.forward(shapesize)
                pen.left(90)
            pen.end_fill()
            keepshape()
        elif firstshape.lower() == "triangle":
            pen.penup()
            pen.goto((shapesize / -2), (shapesize / -2))
            pen.pencolor(firstcolor)
            pen.fillcolor(firstcolor)
            pen.begin_fill()
            pen.pendown()
            for i in range(3):
                pen.forward(shapesize)
                pen.left(120)
            pen.end_fill()
            keepshape()
        elif firstshape.lower() == "circle":
            pen.penup()
            pen.goto(0, (shapesize * -1))
            pen.pencolor(firstcolor)
            pen.fillcolor(firstcolor)
            pen.begin_fill()
            pen.pendown()
            pen.circle(shapesize)
            pen.end_fill()
            keepshape()

keepshape()
        

    


wn = turtle.Screen()
wn.mainloop()