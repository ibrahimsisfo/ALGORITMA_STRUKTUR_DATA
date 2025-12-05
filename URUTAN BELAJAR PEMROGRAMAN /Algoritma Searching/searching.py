def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # indeks ditemukan
    return -1  # tidak ditemukan

data = [11, 6, 9, 0, 2, 7]
cari = 6

hasil = linear_search(data, cari)

if hasil != -1:
    print(f"Data ditemukan pada indeks {hasil}")
else:
    print("Data tidak ditemukan")