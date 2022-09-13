import datetime as dt

username = input("What is your name? ")
print("Hello, " + username + ", welcome to my program.")

age = int(input("How old are you? "))

yearrn = dt.datetime.now().year

birthyear = yearrn - age

def guess():
    firstguess = input("Hmm... I assume you were born in " + str(birthyear) + ". Is this correct? (y/n) ")
    if firstguess.lower() == "y":
        print("Yay! I guessed your birth year.")
    elif firstguess.lower() == "n":
        def run2():
            newbirthyear = birthyear - 1
            secondguess = input("Oh.. were you born in " + str(newbirthyear) + "? (y/n) ")
            if secondguess.lower() == "y":
                print("Yay! I guessed your birth year.")
            elif secondguess.lower() == "n":
                print("Hmm... I couldn't guess your birth year.")
            else:
                print("Invalid response. Must be of either 'y' or 'n'.")
                run2()
        run2()
    else:
        print("Invalid response. Must be of either 'y' or 'n'.")
        guess()

guess()