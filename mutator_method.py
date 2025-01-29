class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def set_brand(self):
        return (self.brand)
    
    def set_model(self):
        return (self.model)
    

c = Car("Ford", "Endavour")

print(c.brand)
print(c.model)