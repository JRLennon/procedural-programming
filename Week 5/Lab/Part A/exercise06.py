def contains_duplicate(numbers):
    return len(set(numbers)) < len(numbers)

numbers = [1, 2, 3, 1]

print(contains_duplicate(numbers))