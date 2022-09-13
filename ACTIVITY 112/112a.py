# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("Making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
colorchoice = input('What color should the circle be? ')
painter.pencolor(colorchoice)


# ask user for the radius of a circle
radiusmoment = int(input('How big should this circle be? (radius) '))

# draw a circle with the radius and line color entered by the user
painter.circle(radiusmoment)

print('Done! Look at your beautiful circle!')

# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()