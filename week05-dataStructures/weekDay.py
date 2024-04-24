# This program prints weather its weekday or not 
# Author : Sarabjeet Kumar

import datetime

# get the today's day
today = datetime.datetime.now().weekday()
print(today) # o t0 4  weekdays // Monday to Friday

if(today < 5 ):
    print("Yes, unfortunately today is a weekday. ");
else:
    print("It is the weekend, yay!");