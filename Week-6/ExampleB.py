# You need to import a file/module in order to use any of its functions.
from MyLib import *
# The * means "imports all functions from that file"

# Now we can use the functions in our code here.
print("Enter an even number. You only have one chance!")

# Remember with method calls that there's always a set of parentheses at the end...
n = promptNumber() # ... Even when you dont give it any parameters
if (isEven(n)):
    print("Well done!")
else:
    print("...")