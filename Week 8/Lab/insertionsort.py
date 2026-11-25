def insertion_sort(array):
    shifts = 0 # count of shifts completed (moving to left)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j+1] = array[j] # shift to the left
            shifts += 1 # increase shifts counter
            j -= 1

        array[j+1] = key
        print(f"After inserting {key}: {array}") # print the list after each element is inserted into its correct position

    print(f"Total shifts: {shifts}")
    return array

# # testing the function with provided values (uncomment to use)
# test_lists = [[9,4,6,2,7], [1,2,3,4,5]]

# for list in test_lists:
#     print(f"\nSorting: {list}")
#     insertion_sort(list.copy())
