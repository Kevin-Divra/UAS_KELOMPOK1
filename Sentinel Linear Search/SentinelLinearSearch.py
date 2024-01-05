import timeit

def LinearSearchSentinel(list1, key, n):
    found = False
    templast = list1[n - 1]
    list1[n - 1] = key
    i = 0

    while list1[i] != key:
        i = i + 1

    list1[n - 1] = templast

    if i < n - 1 or key == list1[n - 1]:
        found = True
        if found:
            print("Target ditemukan pada index ke:")
            print(i)
    else:
        print("Target Tidak Ditemukan")

list1 = [1, 2, 3, 4, 5]
print(list1)
key = int(input("Masukan Target: "))
n = len(list1)
time_taken = timeit.timeit(lambda: LinearSearchSentinel(list1, key, n), number=1)

print(f"Time taken: {round(time_taken, 4)} seconds")
