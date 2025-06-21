class car1:
    name = "Fer"
    kind = "car"
    color = "red"
    value = 60000
    def description(self):
        print(f"Name: {self.name}\nKind: {self.kind}\nColor: {self.color}\nPrice: {self.value}\n")

class car2:
    name = "Jump"
    kind = "car"
    color = "blue"  # Fixed this line
    value = 10000
    def description(self):
        print(f"Name: {self.name}\nKind: {self.kind}\nColor: {self.color}\nPrice: {self.value}\n")

# test code
objOfCar1 = car1()
objOfCar2 = car2()
objOfCar1.description()
objOfCar2.description()
