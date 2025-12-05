#BUBBLE SORTlNg
nama_program="BUBBLE SORTING"
print(nama_program)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

data = [33, 34, 45, 12, 22, 11, 97]
print("Sebelum sorting:", data)
print("Sesudah sorting:", bubble_sort(data))