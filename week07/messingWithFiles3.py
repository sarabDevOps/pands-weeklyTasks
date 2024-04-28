# Checking to see if file exits or not
# Author : Sarabjeet Kumar

import os.path


FILENAME = "count.txt"
if not os.path.isfile(FILENAME):
 print ("File does not exist")
 #initialise file here



def writeNumber(number):
 with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
    f.write(str(number))

writeNumber(0)

def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
 # this file will be created when we write back.
 # no file assumes first time running
 # ie 0 previous runs
        return 0