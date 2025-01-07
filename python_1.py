a = int(input("Enter the value of first number: "))
b = int(input("Enter the value of second number: "))
c = int(input("Enter the value of third number: "))
d = int(input("Enter the value of fourth number: "))

if (a > b) and (a > c) and (a > d):
    print(a, "is greatest")

elif (b > a) and (b > c) and (b > d):
    print(b, "is greatest")

elif(c > a) and (c > b) and (c > d):
    print(c, "is greatest")

# elif (d > a) and (d > b) and (d > c):
#     print(d, "is greatest")

else:
    print(d, "is greatest")

