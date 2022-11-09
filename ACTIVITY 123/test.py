import turtle
import string

window = turtle.Screen()
window.tracer(0)

text = turtle.Turtle()
text.hideturtle()
text.penup()

left_margin = -200
top_margin = 200
line_spacing = 50

text.setposition(left_margin, top_margin)

font = ("Courier", 25)

def write(key):
    text.write(key, font=font)
    text.forward(font[1]*0.65)

def carriage_return():
    text.sety(text.ycor() - line_spacing)
    text.setx(left_margin)

all_characters = string.ascii_letters + string.punctuation + string.whitespace
for key in all_characters:
    window.onkeypress(lambda key=key: write(key), key)

window.onkeypress(carriage_return, "Return")
window.listen()

turtle.done()