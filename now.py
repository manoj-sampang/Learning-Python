class car1:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        print(f"Name: {self.name}\nKind: {self.kind}\nColor: {self.color}\nPrice: {self.value}\n")

class car2:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        print(f"Name: {self.name}\nKind: {self.kind}\nColor: {self.color}\nPrice: {self.value}\n")


objOfCar1 = car1("Fer", "car", "red", 60000)
objOfCar2 = car2("Jump", "car", "blue", "10000")
objOfCar1.description()
objOfCar2.description()
