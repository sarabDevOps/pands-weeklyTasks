# This program asks the user to guess the number untill right number
# Author : Sarabjeet Kumar

numberToGuess = 30
guess = int(input("Please guess the number:"))

while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)
