import random
from bubblesort import bubble_sort
from insertionsort import insertion_sort
from selection_sort import selection_sort

numbers = random.sample(range(1,101), 20)
print(f"Random numbers: {numbers}")

print(f"\nBubble sort:")
bubblesort_result = bubble_sort(numbers.copy())

print(f"\nInsertion sort:")
insertionsort_result = insertion_sort(numbers.copy())

print(f"\nSelection sort:")
selectionsort_result = selection_sort(numbers.copy())

print(f"\nDo the results match: {bubblesort_result == insertionsort_result == selectionsort_result}")

print("Sorted result:", bubblesort_result) # they should all be the same