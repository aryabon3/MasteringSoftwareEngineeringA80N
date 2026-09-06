#06/09/2026
#Created by 480N

# Menu $ Menyimpan data makanan/minuman (Mirip Buku atau Potion).
# Pesanan $ Keranjang belanjaan milik 1 pelanggan (Mirip Inventaris atau Anggota).
# Kasir $ Pengelola transaksi yang menghitung total dan memproses pembayaran (Mirip Perpustakaan).

class Menu:
    def __init__(self, nama_item, harga):
        self.nama_item = nama_item
        self.harga = harga

class Pesanan:
    def __init__(self, nama_pembeli):
        self.nama_pembeli = nama_pembeli
        self.item_dibeli = []

    def tambah_item(self, menu_obj):
        self.item_dibeli.append(menu_obj)
        print(f"{self.nama_pembeli} Menambahkan {menu_obj.nama_item} kedalam pesanan")

    def hitung_total(self):
        total = 0
        for item in self.item_dibeli:
            total += item.harga
        print(total)
        return total

class Kasir:
    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir

    def proses_pembayaran(self, menu_obj, uang_bayar):
        total_tagihan = menu_obj.hitung_total()
        if uang_bayar < total_tagihan:
            print(f"Uang kurang")
        else:
            kembalian = uang_bayar - total_tagihan
            print(f"Pembayaran berhasil, kembalian [{kembalian}]")
        

m1 = Menu("Kopi Hitam", 10)
m2 = Menu("Roti Bakar", 15)
m3 = Menu("Es Teh", 5)

pesanan_arya = Pesanan("Arya")

pesanan_arya.tambah_item(m1)
pesanan_arya.tambah_item(m2)

kasir_warkop = Kasir("Warbel")

kasir_warkop.proses_pembayaran(pesanan_arya, 20)
kasir_warkop.proses_pembayaran(pesanan_arya, 30)