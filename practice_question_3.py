# 3. Operators  
# Q1. Create a program that takes two numbers as input and prints their sum.
# Q2. Write a program that subtracts the second number from the first. Take these two numbers as input.
# Q3.Create a program that multiplies two numbers taken as input.
# Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.
# Q5. Create a program that performs floor division on two numbers. Take these two numbers as input.
# Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.
# Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input.
# Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.
# Q9.Create a program that takes a number as input, increments it, and then decrements it. Print both the incremental and decremental values.
# Q10.Write a program that takes three numbers as input and calculates their average.

# Q1. Create a program that takes two numbers as input and prints their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = a + b

print(c)

print()

# Q2. Write a program that subtracts the second number from the first. Take these two numbers as input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a - b
print(c)

print()

# Q3.Create a program that multiplies two numbers taken as input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = a * b

print(c)

print()

# Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = b / a

print(c)

print()

# Q5. Create a program that performs floor division on two numbers. Take these two numbers as input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = b // a

print(c)

print()

# Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a % b

print(c)
print()

# Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = a ** b
print(c)
print()

# Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.
p = int(input("Enter principle amount: "))
r = int(input("Enter rate of interest: "))
n = int(input("Enter the increament: "))
t = int(input("Enter the time period: "))
a = p * ( 1 + (r / n) ** (n * t))
print(a)
print()

# Q9.Create a program that takes a number as input, increments it, and then decrements it. Print both the incremental and decremental values.
a = int(input("Enter first value: "))
print(a)
print("The increamental value is" + str(a+1) + "And the decreamental value is" + str(a-1))

# Q10.Write a program that takes three numbers as input and calculates their average.
a = int(input("Enter the value of first number: "))
b = int(input("Enter the value of second number: "))
c = int(input("Enter the value of third number: "))
d = (a + b + c / 3)
print(d, "is the average of these number")
print()