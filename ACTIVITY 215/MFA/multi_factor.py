import tkinter as tk
import mfg

min_length = 8
max_length = 24
user_digit = False
user_alpha = False
criteriauser = False
criteriapass = False

user_username = ''
user_password = ''
user_question = ''
user_answer = ''

input_username = input("Enter your username for the restricted application: ")
while criteriauser == False:
    if len(input_username) < 8 or len(input_username) > 24 or input_username.isdigit() or input_username.isalpha():
        if len(input_username) < 8:
            print("Your username is less than 8 characters, which is not allowed.")
        if len(input_username) > 24:
            print("Your username is more than 24 characters, which is not allowed.")
        if input_username.isalpha():
            print("Your username needs to contain a number in it.")
        if input_username.isdigit():
            print("Your username needs to contain a letter in it.")
        input_username = input("Enter your username for the restricted application: ")
    else:
        criteriauser = True
input_password = input("Enter your password for the restricted application: ")
while criteriapass == False:
    if len(input_password) < 8 or len(input_password) > 24 or input_password.isdigit() or input_password.isalpha():
        if len(input_password) < 8:
            print("Your password is less than 8 characters, which is not allowed.")
        if len(input_password) > 24:
            print("Your password is more than 24 characters, which is not allowed.")
        if input_password.isalpha():
            print("Your password needs to contain a number in it.")
        if input_password.isdigit():
            print("Your password needs to contain a letter in it.")
        input_password = input("Enter your password for the restricted application: ")
    else:
        criteriapass = True

my_auth = mfg.MultiFactorAuth()

my_auth.set_authorization("imnotleo1", "Rockfield6!")
auth_info = my_auth.get_authorization()
print(auth_info)

question = "What color is your Bugatti?"
answer = "Orange"
my_auth.set_authentication(question, answer)

my_auth.mainloop()