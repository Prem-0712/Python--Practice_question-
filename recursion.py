def factorial(n = int(input("Enter your number: "))):
    if (n == 0) or (n == 1):
        return (1)
    
    else:
        return ( n * factorial(n - 1))
    
print(factorial())