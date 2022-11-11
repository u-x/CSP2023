#   a123_apple_1.py
from tkinter import scrolledtext
import turtle as trtl
import random as rand
import functools
import string

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
score = 0

scorewriter = trtl.Turtle()
scorewriter.hideturtle()
scorewriter.penup()
scorewriter.goto(0, 210)
scorewriter.pendown()
scorewriter.write("Score: " + str(score), font=("Arial", 20), align="center")

# game variables
ground_height = -200
apple_letter_x_offset = 0
apple_letter_y_offset = -40
letter_font = ("Arial", 45, "bold")
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
listlength = len(letter_list)
current_letter = letter_list.pop(rand.randint(0, listlength-1))

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
# pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def scorepoint():
  global score
  score += 1
  scorewriter.clear()
  scorewriter.write("Score: " + str(score), font=("Arial", 20), align="center")

def draw_apple(active_apple, letter):
  wn.tracer(False)
  global apple_image
  active_apple.shape(apple_image)
  active_apple.penup()
  draw_letter(active_apple, letter)
  wn.tracer(True)
  wn.update()

def draw_pear(active_pear):
  global pear_image
  active_pear.shape(pear_image)
  active_pear.penup()
  wn.update()

def reset_apple(active_apple):
  global current_letter
  listlength = len(letter_list)
  if listlength != 0:
    index = rand.randint(0, listlength-1)
  new_x = rand.randint(-150, 150)
  new_y = rand.randint(-20, 180)
  active_apple.goto(new_x, new_y)
  active_apple.showturtle()
  if len(letter_list) == 0:
    active_apple.goto(0, 0)
    active_apple.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
  else:
    troletter = letter_list.pop(index)
    draw_apple(active_apple, troletter)
    current_letter = troletter


def drop_apple():
  global ground_height, apple
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)
  scorepoint()

def draw_letter(active_apple, letter):
  global apple_letter_x_offset, apple_letter_y_offset, letter_font
  active_apple.color('white')
  pos = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset, active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=letter_font, align="center")
  active_apple.setpos(pos)

def check_apple(letter):
  if current_letter == letter:
    drop_apple()

# def first_fall():
  
#   drop_apple()

# def fall_handler():
#   if current_letter == "A":
#     first_fall()
#   else:
#     drop_apple()


#-----function calls-----
draw_apple(apple, current_letter)
# draw_pear(pear)
# drop_apple(apple)

# drop_apple()

for key in letter_list:
  wn.onkeypress(lambda letter=key: check_apple(letter), key.lower())

wn.onkeypress(lambda letter=current_letter: check_apple(letter), current_letter.lower())
# check_apple("A")

wn.listen()

wn.mainloop()