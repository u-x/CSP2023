import tkinter as tk
import mfg

min_length = 8
max_length = 24
user_digit = False
user_alpha = False
pass_digit = False
pass_alpha = False
criteriauser = False
criteriapass = False

user_username = ''
user_password = ''
user_starpass = ''
user_question = ''
user_answer = ''

input_username = input("Enter your username for the restricted application: ")
while criteriauser == False:
    if len(input_username) < 8 or len(input_username) > 24 or input_username.isdigit() or input_username.isalpha():
        if len(input_username) < 8:
            print("Your username is less than 8 characters, which is not allowed.")
        if len(input_username) > 24:
            print("Your username is more than 24 characters, which is not allowed.")
            user_alpha = False
            user_digit = False
        for placeholder in input_username:
            if placeholder.isalpha():
                user_alpha = True
            if placeholder.isdigit():
                user_digit = True
        if user_alpha == False:
            print("Your password needs to contain a letter in it.")
        if user_digit == False:
            print("Your password needs to contain a number in it.")
        input_username = input("Enter your username for the restricted application: ")
    else:
        criteriauser = True
        user_username = input_username
input_password = input("Enter your password for the restricted application: ")
while criteriapass == False:
    if len(input_password) < 8 or len(input_password) > 24 or input_password.isdigit() or input_password.isalpha():
        if len(input_password) < 8:
            print("Your password is less than 8 characters, which is not allowed.")
        if len(input_password) > 24:
            print("Your password is more than 24 characters, which is not allowed.")
        pass_alpha = False
        pass_digit = False
        for placeholder in input_password:
            if placeholder.isalpha():
                pass_alpha = True
            if placeholder.isdigit():
                pass_digit = True
        if pass_alpha == False:
            print("Your password needs to contain a letter in it.")
        if pass_digit == False:
            print("Your password needs to contain a number in it.")
        input_password = input("Enter your password for the restricted application: ")
    else:
        criteriapass = True
        user_password = input_password

for i in range(len(user_password)):
    user_starpass += "*"

print()
print("username: " + user_username)
print("password: " + user_starpass)

my_auth = mfg.MultiFactorAuth()

my_auth.set_authorization("imnotleo1", "Rockfield6!")
auth_info = my_auth.get_authorization()
print(auth_info)

print("choose a security question from the list below:")
print("1. Mother's maiden name?")
print("2. What is your first car?")
print("3. What color is your Bugatti?")

securityquestionnum = 0

while securityquestionnum == 0 or securityquestionnum >= 4:
    print("Choose a security question from the list below:")
    print("1. Mother's maiden name?")
    print("2. What is your first car?")
    print("3. What color is your Bugatti?")

    securityquestionnum = input("Choose the number of the security question you want to use: ")

    if securityquestionnum.isdigit():
        securityquestionnum = int(securityquestionnum)
    else:
        securityquestionnum = 0
        print("Invalid input. Must be 1-3.")

secanswer = ""

if (securityquestionnum == 1):
    while secanswer.lower() != "jean":
        secanswer = input("What is your mother's maiden name? ")
        if secanswer.lower() == "jean":
            print("Authenticated.")
        else:
            print("Incorrect. Try again.")

if (securityquestionnum == 2):
    while secanswer.lower() != "2015 gmc terrain":
        secanswer = input("What is your first car? ")
        if secanswer.lower() == "2015 gmc terrain":
            print("Authenticated.")
        else:
            print("Incorrect. Try again.")

if (securityquestionnum == 3):
    while secanswer.lower() != "orange":
        secanswer = input("What color is your Bugatti? ")
        if secanswer.lower() == "orange":
            print("Authenticated.")
        else:
            print("Incorrect. Try again.")


question = "What color is your Bugatti?"
answer = "Orange"
my_auth.set_authentication(question, answer)

my_auth.mainloop()