class Car :
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"The car is of {self.brand} {self.model} of {self.year}")

toyota = Car(brand="Toyota", model="Endavour", year="2023")

toyota.start()

print(toyota.model)