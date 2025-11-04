class Siswa:
  
    sekolah = "SMK PGRI 35 Solokanjeruk"

    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    def tampilkan_profil_siswa(self):
        print(f"Nama      : {self.nama}")
        print(f"NIS       : {self.nis}")
        print(f"Kelas     : {self.kelas}")
        print(f"Sekolah   : {Siswa.sekolah}")


s1 = Siswa("Rangga", "12345", "XI TKJ 2")
s2 = Siswa("Dewi", "67890", "XI RPL 1")

s1.tampilkan_profil_siswa()
print()
s2.tampilkan_profil_siswa()