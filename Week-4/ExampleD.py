import math


def main():
    loop = True

    number = 4.5
    print(round(number))
    print(math.ceil(number))
    print(math.floor(number))

    while loop == True:
        user_input = input("Do you want to continue: ").upper()

        if user_input == "NO":
            loop = False


if __name__ == "__main__":
    main()
