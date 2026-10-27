wentindoor3 = False
print("Welcome To The Ice Cream Game! Youre In An Ice Cream Room")

door = input("Choose A Door There Are 3 Doors: ")

if door == "1":
    print("You Escaped The Ice Cream Room! You Win!")
elif door == "2":
    print("You Got Eaten By The Ice Cream Beast! You Lose!")
elif door == "3":
    print("You Got A Sword! Choose Another Door")
    wentindoor3 = True
    door = input("Choose A Door There Are 3 Doors: ")

    if door == "2":
        print("You Ran Into The Ice Cream Beast But You Have A Sword So You Killed It! And You Escaped, So You Win!")
    elif door == "1":
        print("You Escaped The Ice Cream Room! You Win!")
    elif door == "3":
        print("You Picked A Door That Was A Trap! You Lose!")
    else:
        print("Invalid door choice! You Lose!")
else:
    print("Invalid door choice! Please choose 1, 2, or 3.")
