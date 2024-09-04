def main():
    role = "GTA"

    match role:
        case "Student":
            print("The person is a student")
        case "Professor":
            print("The person is a professor")
        case _:
            print("The person is not a student and not a professor")

    number = 3

    match number:
        case 1:
            print("number has a value of 1")
        case 2:
            print("number has a value of 2")
        case 3:
            print("number has a value of 3")


if __name__ == "__main__":
    main()
