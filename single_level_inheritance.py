class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        

    def info(self):
        print(f"The car is {self.brand} {self.model}")

Lamborghini = Car(brand="lamborghini", model="Aventador")
Lamborghini.info()