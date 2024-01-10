import timeit

def search(list1, key):
    list2 = []
    flag = False
    i=0
    for i in range(len(list1)):
        if key == list1[i]:
            flag = True
            list2.append(i)

    if flag:
        print("Target ditemukan pada index ke:")
        for i in list2:
            print(i)
    else:
        print("Target Tidak Ditemukan")

list1 = [1, 2, 3, 4, 5]
print(list1)
key = int(input("Masukan Target:"))
time_taken = timeit.timeit(lambda: search(list1, key), number=1)


print(f"Time taken: {round(time_taken, 4)} seconds")
