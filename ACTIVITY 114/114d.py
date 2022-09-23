def ok():
    #   a114_divisible.py
    print("Think of 2 numbers that are evenly divisible by each other.")
    print()
    # get two numbers from user
    firstnum = int(input("Input a number. "))
    secondnum = int(input("Input a second number. "))

    distancing = float(firstnum / secondnum)

    x = firstnum % secondnum

    # loop while the numbers are not divisible (the remainder is 0)
    while x != 0:
        # inform user of result 
        print("Indivisible")
        print(x)
        # gather user input again
        ok()
    # inform user of result 
    print("Divisible")
    print(x)

ok()