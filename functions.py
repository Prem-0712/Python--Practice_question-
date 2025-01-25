# Defining Function without Parameter
# print('------Defining Function without Parameter-------')
# def add():
#     x = 10
#     y = 20
#     return (x + y)
    

# print(add())

# print()

# #========================================================================

# # Defining Function with Parameter
# print('------Defining Function with one Parameter-------')
# y = "Prem"

# def name (x):
#     print("My name is ", x)

# name(y)

# print()
# #------------------------------------------------------------------------------

# # Defining Function with Parameter
# print('--------Defining Function with Parameter-------')
# def add(x, y):
#     return (x + y)

# print(add(12, 343))

# print()

# #-------------------------------------------------------------------------------

# # Defining multiple function and callling in one function
# print('---- Defining multiple function and callling in one function---')
def add (x, y):
    print("Addition is ", x + y)

def subtract (x, y):
    print("Subtraction is ", x - y)

def multiply (x, y):
    print("Multiplication is ", x * y)

num_1 = 25
num_2 = 20

def calculate():
    add(num_1, num_2)
    subtract(num_1, num_2)
    multiply(num_1, num_2)

calculate()
