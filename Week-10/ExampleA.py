def printList(list):
    for element in list: # For each element in the list myNumbers...
        print(element, end=", ") # Print that element
    print("\n")

def main():
    print("Creating a list...")
    myNumbers = [4, "4", ("Eun Sik", "28")]

    printList(myNumbers)

    print("Adding a new element to the list...")
    myNumbers.append("New element 1")

    printList(myNumbers)

    print("Removing an element from the list...")
    myNumbers.remove("New element 1")

    printList(myNumbers)

if __name__ == "__main__":
    main()