# Provided code is commented out. The fixed code is provided below un-commented

# def total_sum(lst):
#     for x in lst:
#         total = 0
#         total = x + total
#     return total

# # run the function
# print(total_sum([1,2,3,4]))

def total_sum(lst):
    total = 0 # put outside of the for loop, because it kept re-assigning itself to 0
    for x in lst:
        total = x + total
    return total # you could also just do a return sum(lst)

# run the function
print(total_sum([1,2,3,4]))