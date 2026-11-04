def max_difference(list1, list2):
    # get highest of list1
    highest = max(list1)
    lowest = min(list2)
    return(highest - lowest)

list1 = [1, 2, 45]
list2 = [3, 5, 5]

print(f"The largest difference is {max(list1)} - {min(list2)} = {max_difference(list1, list2)}")