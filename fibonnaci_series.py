a = int(input("Enter your number: "))
sum = 0

for i in range ( 0, a + 1 ):
    sum = i + (i - 1)
    print(sum)