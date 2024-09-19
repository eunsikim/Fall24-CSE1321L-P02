# Define a function with 'def' keyword
def fancySubtract(a, b):
    diff = a - b
    if (diff < 0):
        print("Difference below 0!")
    # The return statement is used to stop the method and return a value as a result
    return diff

# Main program code
def main():
    # Making a method call uses the method name, and parameters (here we give a = 3 and b = 5)
    d1 = fancySubtract(3, 5)
    print(d1) # Output: -2
    # Set parameter values explicitly if you want to pass them in a different order.
    d2 = fancySubtract(b=0, a=5)
    print(d2) # Output: 5

if __name__ == "__main__":
    main()
