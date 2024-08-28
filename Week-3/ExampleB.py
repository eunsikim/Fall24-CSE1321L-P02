def main():
    G = 6.67 * pow(10, -11)
    mass1 = float(input("Enter Mass 1: "))
    mass2 = float(input("Enter Mass 2: "))
    distance = float(input("Enter distance between M1 and M2: "))

    # Approach 1
    force = G * mass1 * mass2
    force = force / distance**2
    print(force)

    # Approach 2
    force = (G * mass1 * mass2) / distance**2
    print(force)

    # Approach 3
    top = G * mass1 * mass2
    bot = distance**2
    force = top / bot
    print(force)


if __name__ == "__main__":
    main()
