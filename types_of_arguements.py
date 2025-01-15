# def show (f_name, age):
#     print((f"Name is {f_name} and age is {age}"))

# show("Steve", 100)

# ------------------This is postional arguements-----------

# def show (f_name, age):
#     print((f"Name is {f_name} and age is {age}"))

# show( age= 100, f_name= "Steve")

# ------------------This is type of keyword arguements----------------

# def show (f_name, age = 100):
#     print((f"Name is {f_name} and age is {age}"))

# show( "Steve" )

# ---------------------This is type of default arguement-------------------

# def show ( x, y ):
#     print(x, y)

# show (100, 200)    it won't accept values more than given parameter


# using this star will make it accept value more than given paramater in tuple data type
# def show (*x): 
#     print(x)

# show (100, 200, 300, 400)

# -----------------This is the type of variable length arguement-------------

# def show (**x):
#     print( x["a"], x["b"])

# show (a = 100, b = 200)

# -------------This is the type of keyword variable length arguement ----------------