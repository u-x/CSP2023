#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

# game variables
ground_height = -200
apple_letter_x_offset = 0
apple_letter_y_offset = 0
letter_font = ("Arial", 50, "bold")

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)
wn.bgpic("background.gif")

apple = trtl.Turtle()
# pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  global apple_image
  active_apple.shape(apple_image)
  active_apple.penup()
  
  wn.update()

def draw_pear(active_pear):
  global pear_image
  active_pear.shape(pear_image)
  active_pear.penup()
  wn.update()

def drop_apple():
  global ground_height, apple
  apple.goto(apple.xcor(), ground_height)

def draw_letter(letter, active_apple):
  global apple_letter_x_offset, apple_letter_y_offset
  active_apple.color('white')
  pos = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset, active_apple.ycor() + apple_letter_y_offset)


#-----function calls-----
draw_apple(apple)
# draw_pear(pear)
# drop_apple(apple)
wn.onkeypress(drop_apple, "a")

wn.listen()
wn.mainloop()