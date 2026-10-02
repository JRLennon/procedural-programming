unit_name = "Level 4 Procedural Programming" # assign variable
print("This unit is: ", unit_name) # print variable
print("The 1st character is:", unit_name[0]) # Display first character using index 0
print("The 2nd character is:", unit_name[1]) # Display second character using index 1
print("The 4th character is:", unit_name[3]) # 4th character is of index 4 - 1 = 3
print("The 9th character is:", unit_name[8]) # 9th character is of index 9 - 1 = 8

print(f"The first five characters of the string are: {unit_name[0:5]}") # This should print out just "Level"

print("Changing the number 4 in the string to 100...")
unit_name = unit_name.replace("4", "100") # using .replace to change the 4 into an 100

print(f"This unit is: {unit_name}")