class Kendaraan:
    def __init__(self, merk, plat, harga_sewa):
        self.merk = merk
        self.plat = plat
        self.harga_sewa = harga_sewa

    def get_info(self):
        return f"{self.merk} ({self.plat}) - Rp {self.harga_sewa}/hari"

class Mobil(Kendaraan):
    def __init__(self, merk, plat, harga_sewa, jumlah_pintu):
        super().__init__(merk, plat, harga_sewa)
        self.jumlah_pintu = jumlah_pintu

    def get_info(self):
        return f"{self.merk} ({self.plat}) - Rp {self.harga_sewa}/hari - {self.jumlah_pintu} Pintu"

class Motor(Kendaraan):
    def __init__(self, merk, plat, harga_sewa, type_helm):
        super().__init__(merk, plat, harga_sewa)
        self.type_helm = type_helm

    def get_info(self):
        return f"{self.merk} ({self.plat}) - Rp {self.harga_sewa}/hari - Type Helm: {self.type_helm}"

mobil1 = Mobil("Avanza", "ABC01", 2000, 4)

motor1 = Motor("Kawasaki", "ABC02", 200, "Fullface")

print(mobil1.get_info())
print(motor1.get_info())