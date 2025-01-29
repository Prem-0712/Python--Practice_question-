class Circle:
    pi = 3.14

    def __init__(self):
        self.r = int(input("Enter the radius of your circle: "))

    def area(self):
        return(self.pi * (self.r * 2))
    
c1 = Circle()
print(c1.area())