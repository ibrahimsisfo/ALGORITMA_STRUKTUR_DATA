#IBRAHIM
#D0425013
#UAS PEMROGRAMAN

nama_program="SELECTION SORT"
print(nama_program)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
data = [74, 62, 46, 6, 93, 11]
print("Sebelum sorting:", data)
print("Setelah sorting:", selection_sort(data))