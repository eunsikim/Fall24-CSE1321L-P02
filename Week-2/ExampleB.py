def main():
    number = int(
        input("Enter a number: ")
    )  # Take the input as a String and convert it to an integer
    anotherNumber = int(input("Enter another number: "))

    operation = number / anotherNumber

    print(
        f"The division of {number} / {anotherNumber} is {round(operation, 3)}"
    )  # round(number, decimal places)

    # 2 power of 3
    power = pow(2, 10)  # pow(base, exponent)
    power2 = 2**10
    print(f"POWER: {power}")
    print(f"POWER: {power2}")  # Same operation, different syntax

    # Boolean operations
    # == equals, < less than, > greater than,
    # <= less than or equal, >= greater than or equals
    z = (4 > 3) + (3 > 4)  # True = 1, False = 0, therefore z is (1) + (0) = 1
    print(z)


if __name__ == "__main__":
    main()
