def multiplyByFive(x):
    return x * 5

def main():
    s1 = input("Enter numbers separated by a space: ")

    myList = s1.split(" ") # 1 2 3 => ["1", "2", "3"]

    print(myList)

    myList = list(map(int, myList))

    print(myList)

    myList = list(map(multiplyByFive, myList))

    print(myList)

if __name__ == "__main__":
    main()