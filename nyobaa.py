class Pencarian:
    def __init__(self, karyawan):
        self.karyawan = karyawan

    def cari_karyawan(self, nama):
        if nama in self.karyawan:
            return f"{nama} ditemukan dalam list karyawan"
        else:
            return f"{nama} tidak ditemukan dalam list karyawan"

daftar = Pencarian(['Tyler', 'Ronaldo', 'Jennie', 'Paul', 'Andre'])

nama = input("Masukkan nama karyawan yang ingin Anda cari: ")

print(daftar.cari_karyawan(nama))