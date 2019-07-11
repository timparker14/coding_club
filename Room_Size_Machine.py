def area():
    print("Ok, the room has an area of ", length * width, " Meters.")


def perimeter():
    print("And a perimeter of ", (length + width) * 2, " Meters.")


length = float(input("I will work out the area and perimeter of your room for you.\n"
                     "Please enter the rooms length in meters:\n >"))
width = float(input("Please enter the width of the room in meters:\n >"))
print("Calculating...")
area()
perimeter()


while True:


    def area():
        print("Ok, the room has an area of ", length * width, " Meters.")


    def perimeter():
        print("And a perimeter of ", (length + width) * 2, " Meters.")


    choice = input("Would you like to do another y/n:\n>")
    if choice == "y":
        length = float(input("I will work out the area and perimeter of your room for you.\n"
                             "Please enter the rooms length in meters:\n >"))
        width = float(input("Please enter the width of the room in meters:\n >"))
        print("Calculating...")
        area()
        perimeter()
    else:
        break
print("Ok, Bye :)")