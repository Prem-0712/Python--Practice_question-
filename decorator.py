# def decorator(x):
#     def wrap():
#         print("Before the function is called.")
#         x()
#         print("After the function is called.")
#     return wrap

# def Aven():
#     print("Avengers")

# result = decorator(Aven)
# result()


# print()

# print('------------------------------------')

# def decorate(func):
#     def wrap():
#         print("Before the function is called.")
#         func()
#         print("After the function is called.")
#     return wrap

# @decorate
# def Aven():
#     print("Avengers")

# Aven()


# def decorator ( func ):

#     def wrap():
#         return func().upper()

#     return wrap

# @decorator
# def words():
#     return ("avegers assemble !!")

# print(words())


# def decorator(func):

#     def wrap():
#         return (func() * 2)
    
#     return wrap

# @decorator
# def number():
#     a = int(input("Enter your number: "))
#     return (a)

# print(number())