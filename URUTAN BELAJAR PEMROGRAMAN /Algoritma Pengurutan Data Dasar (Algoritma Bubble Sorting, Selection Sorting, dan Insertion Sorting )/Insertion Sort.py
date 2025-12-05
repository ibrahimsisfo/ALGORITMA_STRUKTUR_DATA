nama_program="INSERTION SORT"
print(nama_program)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = [62, 11, 75, 33, 6]
print("Sebelum sorting:", data)
insertion_sort(data)
print("Setelah sorting :", data)
