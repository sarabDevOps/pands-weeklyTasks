# this reads in a student’s percentage mark and
# prints out corresponding the grade
# Sarabjeet kumar

# takes the percentage into float value coz it has decimal values
percentage = float(input("Type the percentage  "))

if percentage < 0 or percentage > 100:
 
 # Later we will show you error handling
 # This should really throw an error

 print ("Please enter a number between 0 and 100")
elif percentage < 40: # we know it is greater than 0
 print ("Fail")
elif percentage < 50: # between 40 and 49
 print ("Pass")
elif percentage < 60: # between 50 and 59
 print ("Merit1")
elif percentage < 70: # between 60 and 69
 print ("Merit2")
else: # the only option left is between 70 and 100
 print ("Distinction")