def unique_sorted(numbers):
    return(sorted(list(set(numbers)), reverse=True))

uniquenum = [3, 1, 5, 3, 2, 1]

print(unique_sorted(uniquenum))