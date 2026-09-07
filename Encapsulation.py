#Atribut Private (__) & Akses Langsung

#1A
# Buat kelas Dompet yang memiliki satu atribut private: __uang (integer).
# Buat constructor (__init__) yang menerima uang_awal.
# Coba buat objek dompet1 = Dompet(50000).
# Coba akses langsung dengan print(dompet1.__uang) untuk membuktikan bahwa Python akan melempar AttributeError.

# class Dompet:
#     def __init__(self, uang):
#         self.__uang = uang


# dompet1 = Dompet(50000)

# print(dompet1.__uang)

#1B
# Buat kelas Pengguna yang memiliki atribut:
# username (Public)
# __password (Private)
# Buat objek user1 = Pengguna("arya", "rahasia123").
# Cetak username langsung dari luar kelas (harus berhasil).
# Tunjukkan dalam kodenya bahwa __password tidak bisa dicetak langsung dari luar kelas.

# class Pengguna:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

# user1 = Pengguna("Arya", "abonganteng123")

# print(user1.username)
# print(user1.__password)

#2A
# Buat kelas Siswa dengan atribut private __nilai (integer).
# Buat method Getter bernama get_nilai(self) yang mengembalikan nilai dari __nilai.
# Buat objek siswa1 dengan nilai awal 85.
# Cetak nilainya dari luar kelas menggunakan method get_nilai().

class Siswa:
    def __init__(self, nilai):
        self.__nilai = nilai

    def get_nilai(self):
        return self.__nilai

siswa1 = Siswa(85)

print(f"{siswa1.get_nilai()}")

#2B
# Buat kelas KarakterGame dengan atribut public nama dan atribut private __hp (Hit Points, integer).
# Buat method Getter bernama get_hp(self) yang mengembalikan string berformat: "HP [nama]: [__hp]".
# Buat objek karakter, lalu cetak HP-nya menggunakan method getter tersebut.

class KarakterGame:
    def __init__(self, nama, hp):
        self.nama = nama
        self.__hp = hp

    def get_hp(self):
        return f"HP {self.nama}: {self.__hp}"

hero = KarakterGame("Abon", 56)

print(hero.get_hp())

#3A
# Buat kelas Termometer dengan atribut private __celcius (float/integer).
# Buat method Getter get_celcius(self) untuk membaca suhu.
# Buat method Setter set_celcius(self, nilai_baru) dengan validasi:
# Suhu tidak boleh kurang dari -273.15 (Nol Mutlak).
# Jika nilai_baru >= -273.15, ubah nilai __celcius dan cetak "Suhu berhasil diubah".
# Jika kurang, cetak pesan error: "Suhu tidak valid!" dan jangan ubah nilainya.
# Buat objek, lalu tes mengisi suhu yang valid dan suhu yang tidak valid.

class Termometer:
    def __init__(self, celcius):
        self.__celcius = celcius

    def get_celcius(self):
        return f"{self.__celcius}"

    def set_celcius(self, nilai_baru):
        if nilai_baru >= -273.15:
            self.__celcius = nilai_baru
            print("Suhu berhasil diubah")
        else:
            print("Suhu tidak valid")

suhuhu = Termometer(20)

suhuhu.set_celcius(200)
suhuhu.set_celcius(-399)

#3B
# Buat kelas KartuKredit dengan atribut private __limit (integer) dan __pin (integer).
# Buat method Getter get_limit(self) untuk membaca limit.
# Buat method Setter set_limit(self, limit_baru, pin_input) dengan validasi:
# Limit hanya bisa diubah jika pin_input cocok dengan __pin.
# Jika PIN cocok, ubah __limit.
# Jika PIN salah, cetak "PIN Salah! Limit gagal diubah."
# Buat objek, lalu tes mencoba mengubah limit dengan PIN yang salah dan PIN yang benar.

class KartuKredit:
    def __init__(self, limit, pin):
        self.__limit = limit
        self.__pin = pin

    def get_limit(self):
        return f"{self.__limit}"

    def set_limit(self, limit_baru, pin_input):
        if pin_input == self.__pin:
            self.__limit = limit_baru
            print("Limit berhasil diubah")
        else:
            print("PIN Salah! Limit gagal diubah.")

kartu = KartuKredit(100, 123)

kartu.set_limit(200, 123)
kartu.set_limit(200, 1234)