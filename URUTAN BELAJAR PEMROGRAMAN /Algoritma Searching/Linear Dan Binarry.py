nama_program="Linear search"
print(nama_program)
data = [11, 6, 2, 7, 8, 5]

cari = 6
for i in range(len(data)):
    if data[i] == cari:
        print("data ditemukan di indeks", i)

nama_program="Binarry search"
print(nama_program)
data = [4, 6, 5, 3, 1]
cari = 5

low, high = 0, len(data)-1
while low <= high:
    mid = (low + high)//2
    if data[mid] == cari:
        print("data ditemukan di indeks", mid)
        break
    elif data[mid] < cari:
        low = mid + 1
    else:
        high = mid - 1