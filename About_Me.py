# This program says hello and asks for my name.
print('Hi!')
print('What is your name?')
# ask for their name
myName = input()
nameLen = len(myName)
print(nameLen)
message = 'The length of your name is '
print('It is good to meet you, ' + myName)
print(message + str(nameLen) + ' letters.')
print('What is your age?')
# ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
