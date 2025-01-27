class Car: 
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.model} of {self.brand} is starting !!!")

# Ford = Car()
# Toyota = Car()

Ford = Car(year= 2024, model="Endeavour", brand="Ford")
Toyota = Car(brand="Toyota", model="Supraaa", year="1990")

Ford.start()
Toyota.start()