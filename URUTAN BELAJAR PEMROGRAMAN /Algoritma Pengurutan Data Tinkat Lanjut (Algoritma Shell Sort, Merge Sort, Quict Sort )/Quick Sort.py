#QUICK SORT
nama_program="QUICK SORT"
print(nama_program)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  
        kiri = [x for x in arr if x < pivot]
        tengah = [x for x in arr if x == pivot]
        kanan = [x for x in arr if x > pivot]
        return quick_sort(kiri) + tengah + quick_sort(kanan)
data = [10, 7, 8, 9, 1, 5]
print("Hasil Quick Sort:", quick_sort(data))
