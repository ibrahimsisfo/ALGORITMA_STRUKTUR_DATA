#NAMA : IBRAHIM
#NIM : D0425013
#PEMROGRAMAN DASAR

#TUPLE

Riders = ("rossi", "marquez", "lorenzo") #tuple tidak bisa diubah
print("isi tuple: ",Riders)
print("elemen ke-1:", Riders[0])
# Riders[1] = "marquez" #ini akan ERROR karna tuple tidak bisa diubah


#List
Pabrikan = ["movistar yahama", "repsol honda", "ducati corse"] #bisa ubah
print("sebelum diubah:", Pabrikan)

Pabrikan[1] = "ducati corse"  #mengubah isi
Pabrikan.append("suzuki") #menambah data
print("Setelah diubah:", Pabrikan)