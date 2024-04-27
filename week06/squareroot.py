# This program that takes a positive floating-point number as 
# input and outputs an approximation of its square root.
# Author : Sarabjeet Kumar

import math as m

def sqrt(number):
    return m.sqrt(number)
    

sqrt2 = lambda args1 : args1 ** .5;


number = float(input("Please enter a positive number: "))  


print(f"The square root of {number} is ",sqrt(number))
print(f"The square root of {number} is ",sqrt2(number))                         
    