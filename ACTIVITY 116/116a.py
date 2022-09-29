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
angle = 360 / legs
print(angle)
pen.pensize(5)
inc = 0

# draw the legs
while (inc < legs):
  pen.goto(0,20)
  pen.setheading(angle*inc)
  pen.forward(length)
  inc = inc + 1
  print("z*n=", angle*inc)
pen.hideturtle()
wn = trtl.Screen()
wn.mainloop()