#IBRAHIM
#D0425013
#UAS PEMROGRAMAN

nama_program="Binarry search"
print(nama_program)
data = [33, 66, 11, 99, 121]
cari = 11

low, high = 0, len(data)-1
while low <= high:
    mid = (low + high)//2
    if data[mid] == cari:
        print("data ditemukan berada di indeks", mid)
        break

    elif data[mid] < cari:
        low = mid + 1
    else:
        high = mid - 1