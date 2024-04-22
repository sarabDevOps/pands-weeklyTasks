# This program takes the input from console and tell if its even or odd
# Author Sarabjeet Kumar

#  take the input from user 
userNumber = (int)(input("Please type the number ?"))

# check in if and else 
if (userNumber % 2 == 0):
    print("typed number is even ",userNumber)
    print(f"{userNumber} is an even number")

else :
    print("typed number is odd",userNumber)
