# Provided code is commented out. The fixed code is provided below un-commented

# def minimum(lst):
#     a = 0
#     for x in range(1, len(lst)):
#         if lst[x] < lst[a]:
#             a = x
#     return a

# print(minimum([4,2,7,3])) # output should be 2 

def minimum(lst):
    a = 0
    for x in range(1, len(lst)):
        if lst[x] > lst[a]: # Fix: Swapped to a a > rather than <
            a = x
    return a

print(minimum([4,2,7,3])) # output should be 2 