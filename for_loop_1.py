# a = int(input("Enter your number: "))

# for i in range(1, 11):
#     print (a, "*", i, "=", a * i)

# a = int(input("Enter your number: "))

# for j in range (1, (a+1)):
#     for i in range (1, 11):
#         print(j, "*", i, "=", j * i)
#         print()
#     print()
#     print("End of loop")

a = int(input("Enter your number: "))
fact = 1
for i in range (1, a-1):
    fact = fact * i
    i = i - 1
    print(fact)