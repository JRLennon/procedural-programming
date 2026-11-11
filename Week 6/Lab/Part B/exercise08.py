# Provided code is commented out. The fixed code is provided below un-commented

# def find_first_even_number(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             return num
#         else:
#             return None

# # run the function
# result = find_first_even_number([1,3,5,6,7,8])
# print(result)

def find_first_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    else: # Fix: indentation issue
        return None

# run the function
result = find_first_even_number([1,3,5,6,7,8])
print(result)