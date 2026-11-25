def bubble_sort(array):
    swaps = 0
    n = len(array)

    for pass_num in range(n-1):
        swapped_this_pass = False # so we can detect when completed the full sort

        for i in range(n - 1 - pass_num):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i] # Swap them if greater value
                swaps += 1 # Increaese the swap count
                swapped_this_pass = True # We swapped this pass

        print(f"After pass: {pass_num+1}: {array}") # Show progress in the array after each pass (pass_num+1 because zero-indexed)

        if not swapped_this_pass: # If we didn't swap this pass, that means we have completed the sort
            break

    print(f"Total swaps: {swaps}")
    return array

test_lists = [[10,3,6,2,8,1],[1,2,3,4,5],[5,4,3,2,1]]
# arbritatry list, already sorted list, reversed list

for list in test_lists:
    print(f"\nSorting: {list}")
    bubble_sort(list.copy())