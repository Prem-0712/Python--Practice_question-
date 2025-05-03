# n = 5
# for i in range(1, n+1):
#     print("*" * i)


# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)

# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i) + "* " * i )


# n = 5
# for i in range(1, n+1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# a = int(input("Enter number: "))
# original_number = a
# duplicate_number = a
# power= len(str(a))
# sum = 0

# while( a > 0):
#     x = a % 10
#     sum += (x ** power)
#     a //= 10

# if (sum == original_number):
#     print("It's an ARMSTRONG NUMBER ")

# else:
#     print("It's not an ARMSTRONG NUMBER ")


a = int(input("Enter number: "))
original_number = a
power = len(str(a))
sum = 0

while (a > 0):
    x = a % 10
    sum += (x ** power)
    a //= 10

if (sum == original_number):
    print("It's an ARMSTRONG NUMBER")

else:
    print("It's not a ARMSTRONG NUMBER")