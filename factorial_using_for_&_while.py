# ---------------------TOP TO BOTTOM NUMBERS--------------------------------------------

# a = int(input("Enter your number: "))
# i = 0
# while (i <= a):
#     print(i)
#     i = i + 1

# ---------------BOTTOM TO TOP----------------------------------

# a = int(input("Enter your number: "))
# while ( a >= 0):
#     print(a)
#     a = a - 1

# ----------------------FACTORIAL---------------------------------------------

a = int(input("Enter your number: "))
fact = 1
while( a >= 1):
    fact = fact * a
    a = a - 1

# print(fact)


# a = int(input("Enter your number: "))
# i = 1
# fact = 1 

# while( i <= a ):
#     fact = fact * i
#     i = i + 1
# print(fact)

a = int(input("Enter your number: "))
fact = 1
i = a
while( i > 0 ):
    fact = fact * i 
    i = i - 1
print(fact)