def selection_sort(array):
    swaps = 0

    for i in range(len(array) -1):
        min_index = i

        # smallest value in the unsorted part
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # move it to the correct position
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            swaps += 1 # increase swaps counter

        print(f"After pass {i+1}: {array}") # print list after each pass
    print(f"Total swaps: {swaps}")
    return array

# test_lists = [[25,64,11,22,12], [64,25,22,12,11]]

# for list in test_lists:
#     print(f"\nSorting: {list}")
#     selection_sort(list.copy())
