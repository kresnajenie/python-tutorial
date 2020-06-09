class Siswa:
    def __init__(self, nama, alamat, kelas, umur):
        self.nama = nama
        self.alamat = alamat
        self.kelas = kelas
        self.umur = umur

    def print_nama(self, waktu):
        print(f'Selamat {waktu} nama saya {self.nama}')

    def get_nama(self):
        return self.nama

    def edit_nama(self, new_nama):
        self.nama = new_nama

    

siswa = Siswa("Vannes", "Amsterdam", "11A6", 16)
# print(siswa.nama)
# print(siswa.alamat)
# print(siswa.kelas)
# print(siswa.umur)
nama = siswa.get_nama()
print(nama)
siswa.edit_nama(input("Input new name: "))
nama = siswa.get_nama()
print(nama)
