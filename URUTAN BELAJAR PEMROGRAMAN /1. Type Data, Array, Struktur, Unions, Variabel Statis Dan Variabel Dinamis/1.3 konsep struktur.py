class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

m = Mahasiswa("ibrahim", "D0425013")
print(m.nama, m.nim)