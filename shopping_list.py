shopping_list = []
new_item = str
remove_item = str

print("Hi, Let's sort your shopping list.")

while True:

    selection = input("What would you like to do?:\n"
                  "A. View the list\n"
                  "B. Add to list\n"
                  "C. Remove an item from the list\n"
                  "D. Write list to file\n"
                  "Q. Exit\n >")

    if selection == "A":
        print(shopping_list)

    elif selection == "B":
        new_item = input("What would you like to add?:\n >")
        shopping_list.append(new_item)
        print(shopping_list)

    elif selection == "C":
        remove_item = str(input("What would you like to add?:\n >"))
        shopping_list.remove(remove_item)
        print(shopping_list)

    elif selection == "D":
        with open('output.txt', 'w') as filehandle:
            filehandle.writelines("%s\n" % place for place in shopping_list)

    else:
        break
print("Ok, Bye :)")
