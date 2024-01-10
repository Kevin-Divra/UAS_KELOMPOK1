import sys
import os

current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_script_path))
if project_root not in sys.path:
    sys.path.append(project_root)

from time_measurement import time_function, CodeTimer

@time_function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

numbers = [12, 1, 4, -3, 7, 2]

with CodeTimer('Quick Sort'):
    sorted_numbers = quick_sort(numbers)

print(f"Original array: {numbers}")
print(f"Sorted array: {sorted_numbers}")
