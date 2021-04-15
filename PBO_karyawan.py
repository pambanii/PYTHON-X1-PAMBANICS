class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0
 
    def __init__(self, nama, gaji, umur, telepon):
        self.nama = nama
        self.gaji = gaji
        self.umur = umur
        self.telepon = telepon 
        Karyawan.jumlah_karyawan += 1
 
    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)
 
    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print("Umur :", self.umur)
        print("Telepon :", self.telepon)
 
# Membuat objek pertama dari kelas Karyawan
karyawan1 = Karyawan("Sarah", 1000000, 25, 886121)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = Karyawan("Budi", 2000000, 27, 630620)
 
karyawan1.tampilkan_profil()
karyawan2.tampilkan_profil()
print("Total karyawan :", Karyawan.jumlah_karyawan)
