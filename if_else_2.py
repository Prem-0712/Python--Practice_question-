a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a < b) and (b == a + 1) and (c == a + 2):
    print("This is in increasing order.")

elif ( a > b) and ( a == b + 1) and ( b == c + 1):
    print("This is in decreasing order")

else:
    print("It's unordered.")