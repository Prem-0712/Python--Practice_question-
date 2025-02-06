class Vehicle :

    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

class Car (Vehicle):

    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self._color= color

    def start(self):
        print(f"The {self._brand} {self._model} of {self._year},with {self._color} is starting.")

# Toyota = Vehicle(brand="Toyota", model="Endavour", year="2023")

Toyota = Car(brand="Toyota", year="2023", model="Endavour", color="Black")

Toyota.start()