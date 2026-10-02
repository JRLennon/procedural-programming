x = "Here is an example piece of text"
y = 10
z = 5.5

# data types of x,y,z
for i in x,y,z:
    print(f"The type of {i} is {type(i)}.")

# find result nad data type of y + z
result_2 = y + z
print(result_2)
print(type(result_2))

# find result and data type of y + int(z)
result_3 = y + int(z)
print(result_3)
print(type(result_3))

# find the data type of str(z)
result_4 = str(z)
print(type(result_4))

# add x + y?
# print(x + y)
# no, it returns a TypeError. you cannot concatenate an integer and string together

# you could instead convert y to a string first. but that is not practical in this case.

# result_5 = x + str(y)
# print(result_5)
# print(type(result_5)) # this will print out like "Here is an example piece of text10"