a = int(input("Enter your number: "))
i = 1

while (i <= 10):
    print(a, "*", i, "=", a * i)
    i +=1

a = int(input("Enter your number: "))
j = 1

while (j <= a):
    i = 1
    while(i <= 10):
        print(j, "*", i, "=", j * i)
        i += 1
    print()
    print("End of table")
    print()
    j += 1
print()
print("End of loop")