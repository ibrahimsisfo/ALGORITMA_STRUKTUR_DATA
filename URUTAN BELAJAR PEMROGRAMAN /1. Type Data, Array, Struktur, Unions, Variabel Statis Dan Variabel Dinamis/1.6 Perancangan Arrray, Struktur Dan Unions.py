from dataclasses import dataclass
from typing import Union

# ====== UNION (versi Python) ======
@dataclass
class HargaEcer:
    ecer: int

@dataclass
class HargaGrosir:
    grosir: int

# ====== STRUCT ======
@dataclass
class Barang:
    nama: str
    tipe_harga: str   
    harga: Union[HargaEcer, HargaGrosir]


# PROGRAM UTAMA 
daftar_barang = []   # ARRAY untuk menyimpan banyak barang

# Input 3 data barang
for i in range(3):
    print(f"\n=== Data Barang {i+1} ===")
    
    nama = input("Masukkan nama barang: ")
    tipe = input("Pilih tipe harga (ecer/grosir): ").lower()

    if tipe == "ecer":
        nilai = int(input("Masukkan harga ecer: "))
        harga = HargaEcer(nilai)
    else:
        nilai = int(input("Masukkan harga grosir: "))
        harga = HargaGrosir(nilai)

    barang = Barang(nama, tipe, harga)
    daftar_barang.append(barang)     # SIMPAN DI ARRAY


# OUTPUT 
print("\n\n===== DAFTAR BARANG =====")
for idx, b in enumerate(daftar_barang, 1):
    print(f"\nBarang {idx}")
    print("Nama :", b.nama)

    if b.tipe_harga == "ecer":
        print("Harga Ecer   :", b.harga.ecer)
    else:
        print("Harga Grosir :", b.harga.grosir)
