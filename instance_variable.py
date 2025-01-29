class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.brand} {self.model} of {self.year} is starting. ")
    

ford = Car(brand="Ford", model="Endavour", year="2012")

ford.start()