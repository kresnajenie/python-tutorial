class Murid():
    def __init__(self, nama, umur, alamat, kelas):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.kelas = kelas

    def introduce(self):
        return f'Nama saya adalah {self.nama}.\nUmur saya adalah {self.umur}.\nSaya tinggal di {self.alamat}.\nSaya ada di kelas {self.kelas}.'

izaak = Murid("Izaak", 16, "Irian", "11A1")
print(izaak.introduce())
# print(izaak.nama)
# print(izaak.umur)
# print(izaak.alamat)
# print(izaak.kelas)
