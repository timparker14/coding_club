# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('Hello! What is your name?')
myName = input()

print(myName + ' I\'m thinking of a number between 1 and 20. You\'ve got 6 chances to guess it')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
# This condition is the correct guess!
if guess == secretNumber:
    print('Good job! ' + myName + ' You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry ' + myName + ' the number I was thinking of was ' + str(secretNumber))