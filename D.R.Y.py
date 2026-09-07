# Ubah kode di atas agar menerapkan Prinsip DRY menggunakan Inheritance: buat satu Parent Class Minuman,
# lalu jadikan Kopi dan Teh sebagai Child Class-nya!

class Minuman:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Kopi(Minuman):
    pass

class Teh(Minuman):
    pass

kopi = Kopi("Kopi", 5000)
teh = Teh("Teh", 4000)

print(f"{kopi.nama}")
print(f"{kopi.harga}")

print(f"{teh.nama}")
print(f"{teh.harga}")

# Rapikan kode di atas dengan membuat Parent Class AlatMusik yang menampung method stel_nada(),
# sehingga Gitar dan Biola tidak perlu ngetik ulang method tersebut.

class AlatMusik:
    def stel_nada(self):
        print("Menyetel nada instrumen...")

class Gitar(AlatMusik):
    pass

class Biola(AlatMusik):
    pass

gitar = Gitar()
biola = Biola()

gitar.stel_nada()
biola.stel_nada()