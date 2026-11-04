def longest_consecutive(numbers):
    number_set = set(numbers)  # makes it easier to check, reduces duplicates (if any exst)
    longest = 0

    for number in number_set:
        # start the  counting only at the beginning of a sequence
        if number - 1 not in number_set:
            length = 1
            current = number

            # count consecutive numbers
            while current + 1 in number_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


numbers = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(numbers))  # 4
