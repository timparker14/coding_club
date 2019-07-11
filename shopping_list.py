shopping_list = []
new_item = str
remove_item = str

print("Hi, Let's work your shopping list.")

while True:

    selection = input("What would you like to do?:\n"
                      "a. View the list\n"
                      "b. Add to list\n"
                      "c. Remove an item from the list\n"
                      "d. Write list to file\n"
                      "q. Exit\n >")

    if selection == "a":
        print(shopping_list)

    elif selection == "b":
        new_item = input("What would you like to add?:\n >")
        shopping_list.append(new_item)
        print(shopping_list)

    elif selection == "c":
        remove_item = str(input("What would you like to remove?:\n >"))
        print(shopping_list)
        shopping_list.remove(remove_item)
        print(shopping_list)

    elif selection == "d":
        with open('shopping.txt', 'w') as filehandle:
            filehandle.writelines("%s\n" % place for place in shopping_list)

    elif selection == "q":
        print("Ok, bye. :)")
        break

    else:
        print("That's not one of the options. Try again numpty.")
