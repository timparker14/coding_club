
def multiplyer():
    for i in range(1, 11):
        print(i, "X", num, "=", num * i)


num = int(input("Enter the number the times table you would like displayed:\n> "))


print("Multiplication Table of", num)
multiplyer()

while True:
    choice = input("Would you like to do another y/n:\n>")
    if choice == "y":
        num = int(input("Enter the number the times table you would like displayed:\n> "))
        multiplyer()
    else:
        break

print("Bye")