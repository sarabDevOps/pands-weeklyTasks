# Hello world 
# This program prints hello world 
# Author : Sarabjeet Kumar


print ("Hello World!")

print ("Hello ")

answer = 111* 555 

print (answer)

name = input("Enter your name:")
print('Hello ' + name) # if no space input name and hello gonna stuck together

name = input("Enter your name:")
print('Hello '+ name + '\nNice to meet you')
# or you could do this with format
print(f'Hello {name}\nNice to meet you')

number = int(input('please enter a number:'))
newNumber = number + 1
print (f'{number} plus one is {newNumber}')