# 2.Type casting:
#  Q1: Convert an integer to a float. 
# Q2: Convert a float to an integer. 
# Q3: Convert a string to an integer. 
# Q4: Convert a string to a float.
# Q5: Convert an integer to a string. 
# Q6: Convert a float to a string. 
# Q7: Convert a binary string to an integer. 


#  Q1: Convert an integer to a float. 
a = 7
b = float(a)
print(type(a))
print(type(b))

print()

# Q2: Convert a float to an integer. 
a = 10.5
print(int(a))

print()

# Q3: Convert a string to an integer.
a = "5"
print(type(a))
b = a
print(type(int(b)))

print()

# Q4: Convert a string to a float.
a= "5.6"
print(type(a))
b = a
print(type(float(b)))

print()

# Q5: Convert an integer to a string. 
a = 10
print(type(a))
b = a
print(type(str(b)))

print()

# Q6: Convert a float to a string.
a = 10.5
print(type(a))
b = a
print(type(str(b)))

print()

# Q7: Convert a binary string to an integer.
a = "1010"
print(int(a, 2))

