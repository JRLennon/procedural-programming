# Error code commented here:

# numbers = [10,20,30,40]
# index = int(input("Enter an index number: "))
# divisor = int(input("Enter a divisor: "))

# result = numbers[index] / divisor
# print("Result: ", result)

numbers = [10,20,30,40]
try:
    index = int(input("Enter an index number: "))
    divisor = int(input("Enter a divisor: "))

    result = numbers[index] / divisor
    print("Result: ", result)
except ValueError:
    print("You must enter an integer - please try again.")
except IndexError:
    print("You must enter an index lower than 4 - please try again.")
except Exception:
    print("Unknown error ocurred - Please try again.")

"""
Question answers:
1. What type of error occurs in each case?
- Word instead of number returns a "ValueError: invalid literal for int() with base 10: 'hskjdhsajkdsa'"
- Index larger than 3 returns an "IndexError: list index out of range"
2. Modify the program to handle these errors using try-except.
- Completed - added two except blocks ValueError and IndexError
3. Can you use multiple except blocks to handle different errors?
- Yes, you can use different except blocks to handle different types of errors (exceptions) that might happen.
4. Can you catch other unexpected errors using a general except block?
- Yes, you can use a normal Exception block to catch any other exceptions that were not previously caught
"""