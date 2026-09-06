class Potion:
    def __init__(self, nama, heal_amount):
        self.nama = nama
        self.heal_amount = heal_amount

class Inventaris:
    def __init__(self):
        self.daftar_potion = []

    def tambah_item(self, potion_obj):
        self.daftar_potion.append(potion_obj)
        print(f"[I] Barang berupa {potion_obj.nama} berhasil di masukan")

    def ambil_item(self):
        if not self.daftar_potion:
            print(f"[i] Tas Kosong")
            return None

        item_keluar = self.daftar_potion.pop()
        print(f"[i] {item_keluar.nama} berhasil diambil")
        return item_keluar

class Hero:
    def __init__(self, nama, hp, max_hp = 100):
        self.nama = nama
        self.hp = hp
        self.max_hp = max_hp
        self.tas = Inventaris()

    def terkena_serangan(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

        print(f"[{self.nama}] terkena serangan {damage}")
        print(f"Sisa HP {self.nama}: {self.hp}")

    def minum_potion(self, potion_obj):
        self.hp += potion_obj.heal_amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"[{self.nama}] minum obat {potion_obj.nama}")
        print(f"Sisa HP {self.nama}: {self.hp}")

    def serang(self, lawan_hero, damage):
        lawan_hero.hp -= damage

        if lawan_hero.hp < 0:
            lawan_hero.hp = 0

        print(f"[{lawan_hero.nama}] terkena serangan oleh {self.nama} sebesar: {damage} damage")
        print(f"Sisa HP {lawan_hero.nama}: {lawan_hero.hp}")

    def simpan_item(self, potion_obj):
        print(f"{self.nama} Memasukan barang ke tas")

        self.tas.tambah_item(potion_obj)

    def gunakan_item(self):
        item = self.tas.ambil_item()

        if item != None:
            self.minum_potion(item)
        else:
            print("Tidak ada apa apa")

arya = Hero("Arya", 100)

anggur = Potion("Anggur", 50)
apel = Potion("Apel", 80)

arya.simpan_item(anggur)
arya.simpan_item(apel)

arya.terkena_serangan(90)

arya.gunakan_item()