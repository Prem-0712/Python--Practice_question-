class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return(self.brand)
    
    def get_model(self):
        return (self.model)
    
c= Car('Ford','Mustang')
print(c.get_brand())
print(c.get_model())

print()

print(f'Maker of Car is {c.brand}')
print(f'Model of Car is {c.model}')