# This program asks the user to input int 
# Taking the current value and, if it is even, divide it by two,
# but if it is odd, multiply it by three and add one.

userInput = int(input("Type the number : "))
#print(userInput)
userList = []
while(userInput != 1):
    print(userInput)
    userList.append(userInput)
    if (userInput % 2 == 0):
        userInput = userInput/2 
    else :
        userInput = (userInput * 3 + 1)

userList.append(userInput)
print(userInput)
print(userList)