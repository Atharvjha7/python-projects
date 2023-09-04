import time
import random
import sys
print("This is a sorting algorithim comparison that reports time and space complexity, as well as Big O. ")
print("Each algorithim will be using the same data set of 10,000 randomly generated values.")
# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Random pivot selection

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Function to measure space complexity
def measure_space(func, *args):
    before = sys.getsizeof(args[0])
    func(*args)
    after = sys.getsizeof(args[0])
    return after - before

# Generate a random list of numbers
random_list = [random.randint(1, 10000) for _ in range(10000)]

# Algorithms to test
sorting_algorithms = [
    ("Selection Sort", selection_sort, "O(n^2)"),
    ("Insertion Sort", insertion_sort, "O(n^2)"),
    ("Bubble Sort", bubble_sort, "O(n^2)"),
    ("Merge Sort", merge_sort, "O(n log n)"),
    ("Quick Sort", quick_sort, "O(n^2) average, O(n log n) with random pivot")
]

# Perform sorting and measure space complexity
for name, algorithm, big_o in sorting_algorithms:
    arr = random_list.copy()
    print(f"Sorting using {name}.")
    start_time = time.time()
    space_complexity = measure_space(algorithm, arr)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{name} - Time: {execution_time:.6f} seconds, Space: {space_complexity} bytes, Big O: {big_o}")
    print()

# Measure space complexity for Python's built-in sorted function
arr = random_list.copy()
print("Sorting using Python's Sorted function.")
start_time = time.time()
space_complexity = measure_space(sorted, arr)
end_time = time.time()
execution_time = end_time - start_time
print(f"Python's Sorted - Time: {execution_time:.6f} seconds, Space: {space_complexity} bytes, Big O: O(n log n)")
