import turtle as trtl

pen = trtl.Turtle()

print()
print()
print("Making a circle...")
print()

# ask user for a color (such as red, green, blue, pink, purple)
colorchoice = input('What color should the circle be? ')
pen.pencolor(colorchoice)


# ask user for the radius of a circle
radiusmoment = int(input('How big should this circle be? (radius) '))

print("A full circle is 360 degrees.")
angle = int(input("What angle should this circle go around? "))

segments = int(input("How many segments (lines) should the circle have? "))

pen.penup()
pen.goto(0, (radiusmoment * -1))
pen.pendown()
pen.fillcolor(colorchoice)

pen.begin_fill()

# draw a circle with the radius and line color entered by the user
pen.circle(radiusmoment, angle, segments)

pen.end_fill()

print('Done! Look at your beautiful circle!')

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()