class Fact:
    def __init__(self):
        self.a = int(input("Enter your number: "))

    def input(self):
        factorial = 1

        for i in range(self.a):
            factorial *= (i + 1)
        
        print(factorial)

classwork = Fact()
classwork.input()