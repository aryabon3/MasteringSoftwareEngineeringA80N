# Buat Parent Class Notifikasi dengan method kirim() yang mencetak "Mengirim notifikasi umum...".
# Buat Child Class EmailNotifikasi yang menimpa (override) method kirim() agar mencetak "Mengirim notifikasi via Email!".
# Buat objek dari EmailNotifikasi dan panggil method kirim().

class Notifikasi:
    def kirim(self):
        print("Mengirim notifikasi umum...")

class EmailNotifikasi(Notifikasi):
    def kirim(self):
        print("Mengirim notifikasi via Email!")

email = EmailNotifikasi()

email.kirim()

# Buat Parent Class Siswa yang punya method belajar() (mencetak "Siswa sedang belajar umum").
# Buat Child Class SiswaAutomotif yang menimpa method belajar() agar mencetak "Siswa sedang praktik servis mesin di bengkel!".
# Buat objek dari SiswaAutomotif dan panggil method belajar().

class Siswa:
    def belajar(self):
        print("Siswa sedang belajar umum")

class SiswaAutomotif(Siswa):
    def belajar(self):
        print("Siswa sedang praktik servis mesin di bengkel!")

abon = SiswaAutomotif()

abon.belajar()