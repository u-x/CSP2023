#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    okthen = floor % 21
    painter.goto(x, y)
    painter.color("red")
    y = y + 5 # location of next floor
    rem = floor % 6
    print(rem)
    if rem > 2:
        painter.color("blue")
    #draw the floor
    painter.pendown()
    painter.forward(50)
    if okthen == 20:
        x = x + 60
        y = -150
    

wn = trtl.Screen()
wn.mainloop()