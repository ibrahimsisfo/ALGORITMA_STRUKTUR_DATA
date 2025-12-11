#IBRAHIM
#D0425013
#UAS PEMROGRAMAN

nama_program="INTERPOLATION SEARCH"
print(nama_program)

def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:

        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))
        
        print(f"Memeriksa posisi indeks: {pos}")

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1
    return -1

data = [11, 22, 33, 44, 55, 66, 77]
cari = 66

hasil = interpolation_search(data, cari)

if hasil != -1:
    print(f"Data {cari} ditemukan berada pada indeks ke-{hasil}")
else:
    print(f"Data {cari} tidak ditemukan")