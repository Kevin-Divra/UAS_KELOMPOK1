import time
from time_measurment import CodeTimer, time_function

@time_function
def fibonacci_search(arr, x):
    fib_2 = 0
    fib_1 = 1
    fib_m = fib_2 + fib_1

    while fib_m < len(arr):
        fib_2 = fib_1
        fib_1 = fib_m
        fib_m = fib_2 + fib_1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_2, len(arr) - 1)

        if arr[i] < x:
            fib_m = fib_1
            fib_1 = fib_2
            fib_2 = fib_m - fib_1
            offset = i
        elif arr[i] > x:
            fib_m = fib_2
            fib_1 = fib_1 - fib_2
            fib_2 = fib_m - fib_1
        else:
            return i

    if fib_1 and arr[offset + 1] == x:
        return offset + 1

    return -1

if __name__ == "__main__":
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    x = 85
    
    print(f"Data yang dicari: {x}")
    print(f"Data yang ada dalam array: {arr}")

    with CodeTimer("Fibonacci Search"):
        result = fibonacci_search(arr, x)
    
    if result != -1:
        print(f"\nTarget ditemukan di indeks: {result}")
    else:
        print("\nTarget tidak ditemukan")