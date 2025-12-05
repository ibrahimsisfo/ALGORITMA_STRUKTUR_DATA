#SHELL SORT
nama_program="SHELL SORT"
print(nama_program)
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp      
        gap //= 2
data = [11, 62, 6, 66, 26, 33, 1, 3]
shell_sort(data)
print("Hasil Shell Sort:", data)