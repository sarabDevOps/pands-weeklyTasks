# This program reads in string and convert into lowerCase
# Strips any trailing spaces
# It also converts it to lower case
# and the normalised one
# Author Sarabjeet Kumar


getString = input("Please enter the String : ");
normalizsString = getString.strip().lower();

print(f'Normsilze string is {normalizsString}')


lenghtOfInputString = len(getString)
lenghtOfNormalizedString = len(normalizsString)

print(f'length of inputString  : {lenghtOfInputString}  and lenght of narmalisedString is {lenghtOfNormalizedString}  ')