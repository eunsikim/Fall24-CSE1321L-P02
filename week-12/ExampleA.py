class PC:
    def __init__ (self, MB, CPU, RAM, SSD):
        self.MB = MB
        self.CPU = CPU
        self.RAM = RAM
        self.SSD = SSD
        self.power = False

    def turnOn(self):
        self.power = True
        print("PC is on")
    
    def turnOff(self):
        self.power = False
        print("PC is off")

def main():
    pc1 = PC("ASUS", "Intel i7", "16GB", "1TB")
    pc2 = PC("MSI", "AMD Ryzen 5", "8GB", "512GB")

    print(pc1.MB)
    print(pc2.MB)

    pc1.MB = "Gigabyte"

    print(pc1.MB)
    print(pc2.MB)

    if not pc1.power:
        print("PC 1 is off")
        pc1.turnOn()
    
    if pc1.power:
        print("PC 1 is on")
        pc1.turnOff()

if __name__ == "__main__":
    main()