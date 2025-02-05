from abstract import Shape

class Square( Shape ):

    def __init__(self):
        self.side = int(input("Enter your number: "))

    def area(self):
        return ( (self.side) ** 2)
    
    def perimeter(self):
        return ( (self.side) * 4)