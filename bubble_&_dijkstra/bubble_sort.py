import functools
import time

def time_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) * 1000.0
        print(f"Function '{func.__name__}' executed in {run_time:.2f} ms")
        return result
    return wrapper

@time_function
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return

arr = [99, 436, 25, 12, 22, 7, 67]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
    
    
    #table complexity in big o notation for bubblesort
    #O(n^2)