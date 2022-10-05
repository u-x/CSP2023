my_courses = ["Math", "English", "Science", "History"]
def pleasework():
    for course in my_courses:

        print() # blank line
        print("Enter your points for " + course)

        points = int(input("Points -> "))

        if (points >= 90):
            print("A")
        elif (points >= 80):
            print("B")
        elif (points >= 70):
            print("C")
        elif (points >= 60):
            print("D")
        else:
            print("F")

pleasework()
redo = input("Do you need to re-do these grades? (y/n)")
while (redo == "y"):
    redo = "n"
    pleasework()
    redo = input("Do you need to re-do these grades? (y/n)")
