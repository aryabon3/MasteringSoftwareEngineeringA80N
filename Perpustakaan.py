class Buku:
    def __init__(self, judul, penulis, status = True):
        self.judul = judul
        self.penulis = penulis
        self.status = status

class Anggota:
    def __init__(self, nama, id, max_pinjam = 2):
        self.nama = nama
        self.id = id
        self.daftar_pinjam = []
        self.max_pinjam = max_pinjam

    def tambah_buku(self, buku_obj):
        if len(self.daftar_pinjam) == self.max_pinjam:
            print(f"Anda sudah meminjam {self.max_pinjam} buku")
            return False
        else:
            self.daftar_pinjam.append(buku_obj)
            return True

    def kembalikan_buku(self, buku_obj):
        if buku_obj in self.daftar_pinjam:
            self.daftar_pinjam.remove(buku_obj)
            return True
        else:
            return False

class Perpustakaan:
    def __init__(self, nama_perpus):
        self.nama_perpus = nama_perpus
        self.katalog = []

    def tambah_buku(self, buku_obj):
        self.katalog.append(buku_obj)
        print(f"Buku dengan judul {buku_obj.judul} berhasil dimasukan kedalam katalog")

    def pinjam_buku(self,anggota_obj, buku_obj):
        if buku_obj.status == False:
            print(f"Buku '{buku_obj.judul}' Lagi di pinjem orang")
            return

        berhasil = anggota_obj.tambah_buku(buku_obj)

        if berhasil:
            buku_obj.status = False
            print(f"{anggota_obj.nama} berhasil meminjam buku '{buku_obj.judul}'.")

    def kembalikan_buku(self, anggota_obj, buku_obj):
        berhasil = anggota_obj.kembalikan_buku(buku_obj)

        if berhasil:
            buku_obj.status = True
            print(f"{anggota_obj.nama} berhasil mengembalikan buku '{buku_obj.judul}'.")
        else:
            print(f"{anggota_obj.nama} tidak sedang meminjam buku '{buku_obj.judul}'.")

perpustakaan = Perpustakaan("Jakarta Fair")

b1 = Buku("Laskar Pelangi", "Arya")
b2 = Buku("Tere Liye", "Abon")
b3 = Buku("Cinta 2", "Anin")

perpustakaan.tambah_buku(b1)
perpustakaan.tambah_buku(b2)
perpustakaan.tambah_buku(b3)

anggota1 = Anggota("Arya", "ABC01", 2)

perpustakaan.pinjam_buku(anggota1, b1)
perpustakaan.pinjam_buku(anggota1, b2)

perpustakaan.kembalikan_buku(anggota1, b2)

perpustakaan.pinjam_buku(anggota1, b3)