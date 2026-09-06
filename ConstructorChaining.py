# Buat Parent Class Bentuk dengan atribut warna.
# Buat Child Class Persegi yang punya atribut warna (diurus oleh super()) dan atribut khusus sisi (integer).
# Buat objek Persegi berwarna "Merah" dengan sisi 5.
# Cetak warna dan sisinya.

class Bentuk:
    def __init__(self, warna):
        self.warna = warna

class Persegi(Bentuk):
    def __init__(self, warna, sisi):
        super().__init__(warna)

        self.sisi = sisi

persegi = Persegi("Merah", 5)
print(f"Persegi warna: {persegi.warna} dengan {persegi.sisi} sisi")

# Buat Parent Class Akun dengan atribut username dan email.
# Buat Child Class AkunPremium yang menggunakan super() untuk username dan email,
# serta menambahkan atribut khusus fitur_vip (boolean, contoh: True).
# Buat objek AkunPremium dan cetak ketiga atributnya.

class Akun:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class AkunPremium(Akun):
    def __init__(self, username, email, fitur_vip = False):
        super().__init__(username, email)
        self.fitur_vip = fitur_vip

premium = AkunPremium("abon", "abon@gmail.com", True)
print(f"Halo {premium.username}, email kamu adalah {premium.email} fitur VIP kamu: {premium.fitur_vip}")