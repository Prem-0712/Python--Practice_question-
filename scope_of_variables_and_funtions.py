x = 100

def show ():
    x = 200
    x = globals()["x"]

    print("Variable inside function: ", x)
    print("Variable inside function: ", x)

show()

print("Variable outside function", x)

