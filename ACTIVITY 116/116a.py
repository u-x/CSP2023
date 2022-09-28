#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name pen is used
pen = trtl.Turtle()
pen.pensize(40)
pen.circle(20)
legs = 7
y = 70
z = 380 / legs
pen.pensize(5)
n = 0
while (n < legs):
  pen.goto(0,0)
  pen.setheading(z*n)
  pen.forward(y)
  n = n + 1
pen.hideturtle()
wn = trtl.Screen()
wn.mainloop()