a = int(input("Enter your number: "))
sum = 0

while ( a >= 0):
    x = a % 10
    a = a // 10
    sum = x + a
print(sum)