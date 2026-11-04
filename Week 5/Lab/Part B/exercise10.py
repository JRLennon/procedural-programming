def two_sum(numbers, target):
    # check each pair of numbers in the list
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                # found the correct pairing
                return [i, j]
    
    # return an empty list if no pairing is found
    return []

numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))  # [0, 1]