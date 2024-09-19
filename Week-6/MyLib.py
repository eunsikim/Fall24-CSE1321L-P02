# MyLib has some method definitions...
def isEven(num):
    # If num is even, then num % 2 must be 0.
    if (num % 2 == 0):
        print(str(num) + " is even!")
        return True
    else:
        print(str(num) + " is odd.")
        return False
def promptNumber():
    text = input("Enter a number, please: ")
    num = int(text)
    return num

# ... But no "main" code. (so running this file doesn't print anything)