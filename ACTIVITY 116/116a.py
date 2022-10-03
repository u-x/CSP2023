#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name pen is used
pen = trtl.Turtle()
pen.pensize(40)

# create spider body
pen.circle(20)

# spider leg config
legs = 8
length = 70
angle = 25
pen.pensize(5)
inc = 0

# draw the legs
while (inc < legs):
  pen.goto(0,20)
  if (inc > 3):
    pen.setheading(angle*inc+45)
  else:
    pen.setheading(angle*inc-45)
  pen.forward(length)
  inc = inc + 1
pen.hideturtle()
pen.pu()
pen.goto(-15, 30)
pen.color("white")
pen.dot(20)
pen.color("black")
pen.dot(10)
pen.goto(15, 30)
pen.color('white')
pen.dot(20)
pen.color('black')
pen.dot(10)
wn = trtl.Screen()
wn.mainloop()