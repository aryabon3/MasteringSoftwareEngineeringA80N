class Karakter:
    def __init__(self, nama, hp, level):
        self.nama = nama
        self.__hp = hp
        self.__level = level

    def get_hp(self):
        return self.__hp

    def get_level(self):
        return self.__level

    def add_hp(self, jumlah):
        self.__hp += jumlah

    def terima_serangan(self, damage):
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
            print(f"{self.nama}: Telah mati")
        else:
            print(f"{self.nama}: Telah menerima {damage} damage. Sisa HP: {self.get_hp()}")

    def get_info(self):
        return print(f"[{self.nama} | Lv.{self.get_level()} | HP: {self.get_hp()}]")

class Kesatria(Karakter):
    def __init__(self, nama, hp, level, armor):
        super().__init__(nama, hp, level)
        self.__armor = armor

    def terima_serangan(self, damage):
        damage_hp = damage - self.__armor
        if damage_hp < 0:
            damage_hp = 0

        super().terima_serangan(damage_hp)

    def get_info(self):
        return print(f"[{self.nama} | Lv.{self.get_level()} | HP: {self.get_hp()} | Armor: {self.__armor}]")

class Penyihir(Karakter):
    def __init__(self, nama, hp, level, mana):
        super().__init__(nama, hp, level)
        self.__mana = mana

    def sihir_pulih(self):
        if self.__mana >= 10:
            self.__mana -= 10
            self.add_hp(30)
            print(f"{self.nama} Menggunakan sihir pemulihan!, mana tersisa: {self.__mana}")
        else:
            print(f"Mana tidak cukup")

    def get_info(self):
        return print(f"[{self.nama} | Lv.{self.get_level()} | HP: {self.get_hp()} | Mana: {self.__mana}]")

ksatria = Kesatria("Abon", 100, 5, 10)
mage = Penyihir("Ibnu", 80, 5, 25)

ksatria.get_info()
mage.get_info()

ksatria.terima_serangan(25)
mage.sihir_pulih()

ksatria.get_info()
mage.get_info()