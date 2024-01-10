import time
from time_measurment import CodeTimer, time_function

@time_function
def Binary_Search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    data = [2, 4, 8, 16, 32]
    target = 16 
    
    print(f"Data yang dicari: {target}")
    print(f"Data yang ada dalam array: {data}")    
    
    with CodeTimer("BinarySearch"):
        result = Binary_Search(data, target)
    
    if result != -1:
        print(f"\nTarget ditemukan di indeks: {result}")
    else:
        print("\nTarget tidak ditemukan")

    
    
    
