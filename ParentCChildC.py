# Buat Parent Class bernama Pegawai yang punya atribut nama dan gaji.
# Lalu buat Child Class bernama Manager yang mewarisi Pegawai.
# Buat 1 objek dari kelas Manager dengan nama "Budi" dan gaji 10000000.
# Cetak nama dan gaji dari objek manager tersebut (harus terbukti kalau Manager bisa mengakses atribut milik Pegawai).

#NOMOR 1
#Parent Class
class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    
#Child Class
class Manager(Pegawai):
    def cetak(self):
        print(f"Nama: {self.nama} dengan Gaji: {self.gaji}")

pegawai1 = Manager("Budi", 10000000)

pegawai1.cetak()


# Buat Parent Class bernama Elektronik yang punya method nyalakan() (mencetak "Perangkat menyala").
# Buat Child Class bernama Laptop yang mewarisi Elektronik dan punya method khusus ketik() (mencetak "Sedang mengetik...").
# Buat objek laptop, lalu panggil method nyalakan() dan ketik().

#NOMOR 2
#Parent Class
class Elektronik:
    def __init__(self):
        pass

    def nyalakan(self):
        print("Perangkat menyala")

class Laptop(Elektronik):
    def ketik(self):
        print("Laptop sedang mengetik")

laptop1 = Laptop()

laptop1.nyalakan()
laptop1.ketik()