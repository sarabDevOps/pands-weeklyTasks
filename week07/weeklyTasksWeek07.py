# This is a weekly task week 07
# Reads how many e'S 

FILENAME = input("Enter the file name: ")



def readsFromFile(FILENAME):
    try:
        with open(FILENAME, 'r') as file:
            content = file.read()
            count = 0
            for char in content:
             if char == 'e':
                count += 1        
            return count
    except FileNotFoundError:
        print("Error: File '{}' not found.".format(FILENAME))


print(readsFromFile(FILENAME ))