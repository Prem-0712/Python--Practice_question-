# def factorial (n):
#     if (n == 1) or (n == 0):
#         return 1
    
#     else:
#         return n * factorial( n - 1)
    
# n = int(input("Enter your number: "))

# print(f"The factorial of your number is {factorial(n)}")

# def fibonacci (n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# n = int(input("Enter your number: "))
# print(f"The fibonacci series of {n} is {fibonacci(n)}")

def sum_of_digits (n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)
    
n = int(input("Enter your number: "))
print(f"The sum of your digits are {sum_of_digits(n)}")