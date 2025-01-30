class Car():
    
    def __init__(self):
        print("This is parent class constructor")

class vehicle (Car):

    def __init__(self):
        print("This is child class constructor")
        super().__init__()

Ford = vehicle()