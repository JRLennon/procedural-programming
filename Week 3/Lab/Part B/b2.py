user_int = int(input("Please enter an integer: "))

# pos, neg, zero
if user_int >0:
    print("Positive number")
elif user_int <0:
    print("Negative number")
elif user_int == 0:
    print("Zero")
else:
    print("Unable to calculate whether the entered integer is positive, negative, or zero.")

# if pos, check if even or odd
if user_int >0:
    print("Even number") if user_int %2 == 0 else print("Odd number")

# if large num
print("This is a large number.") if user_int >100 else None