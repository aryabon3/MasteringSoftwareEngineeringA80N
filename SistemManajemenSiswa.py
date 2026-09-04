#========================================
#Sistem Manajemen & Analisis Nilai Siswa
#========================================

siswa = [
    {"nama": "Arya", "mtk": 50, "bing": 80, "bind": 70, "status": "Unknown", "total_nilai": 0, "rata_rata": 0},
    {"nama": "Anin", "mtk": 100, "bing": 100, "bind": 100, "status": "Unknown", "total_nilai": 0, "rata_rata": 0}
]

ditemukan = False


def input_data_siswa():
    jumlah_siswa = int(input("Masukan jumlah siswa yang mau di input: "))
    for i in range(jumlah_siswa):
        nama = input("Masukin Nama: ")
        mtk = int(input("Masukin Nilai MTK: "))
        bing = int(input("Masukin Nilai BING: "))
        bind = int(input("Masukin Nilai BIND: "))
        total_nilai = mtk + bing + bind
        rata_rata = total_nilai / 3
        if rata_rata >= 75:
            status = "Lulus"
        elif rata_rata < 75:
            status = "Tidak Lulus"
        siswa_baru = {"nama": nama, "mtk": mtk, "bing": bing, "bind": bind, "status":status, "total_nilai": total_nilai, "rata_rata": rata_rata}
        siswa.append(siswa_baru)

def rekap_kelas():
    juara_kelas = ""
    ranking_bawah = ""
    if not siswa:
        print("G ada data jir")
        input()
    else:
        total_rata_rata_kelas = 0
        rata_rata_tertinggi = 0
        rata_rata_kelas = 0
        rata_rata_terendah = 100
        for i in range(len(siswa)):
            total_rata_rata_kelas += siswa[i]["rata_rata"]

            if siswa[i]["rata_rata"] > rata_rata_tertinggi:
                rata_rata_tertinggi = siswa[i]["rata_rata"]
                juara_kelas = siswa[i]["nama"]

            if siswa[i]["rata_rata"] < rata_rata_terendah:
                rata_rata_terendah = siswa[i]["rata_rata"]
                ranking_bawah = siswa[i]["nama"]

        rata_rata_kelas = total_rata_rata_kelas / len(siswa)
        
        print(f"Rata Rata Kelas: {rata_rata_kelas}")
        print(f"Ranking 1: {juara_kelas} dengan Rata Rata: {rata_rata_tertinggi}")
        print(f"Ranking {len(siswa)}: {ranking_bawah} dengan Rata Rata: {rata_rata_terendah}")

        input()

def cari_siswa(nama):
    ditemukan = False
    for s in siswa:
        if s["nama"].lower() == nama.lower():
            print(f"Nama: {s['nama']}\nRata Rata: {s['rata_rata']}\nStatus: {s['status']}")
            ditemukan = True
            break

    if not ditemukan:
        print("Tidak ada nama siswa tersebut")
    input()

def hapus_siswa(nama):
    ditemukan = False
    for s in siswa:
        if s["nama"].lower() == nama.lower():
            siswa.remove(s)
            ditemukan = True
            break

    if not ditemukan:
        print("Tidak ada nama siswa tersebut")
    input()

#rata rata siswa
for i in range(len(siswa)):
    siswa[i]["total_nilai"] = siswa[i]["mtk"] + siswa[i]["bing"] + siswa[i]["bind"]
    siswa[i]["rata_rata"] = siswa[i]["total_nilai"] / 3

    #status siswa
    if siswa[i]["rata_rata"] > 75:
        siswa[i]["status"] = "Lulus"
    else:
        siswa[i]["status"] = "Tidak Lulus"


#==========LIST===========
while True:
    print("1. Tambah Data Siswa Baru")
    print("2. Tampilkan Data Seluruh Siswa")
    print("3. Rekap Kelas")
    print("4. Cari Siswa")
    print("5. Hapus Siswa")
    print("6. Keluar")
    pilih_menu1 = int(input("Pilih Menu (1-6): "))

    if pilih_menu1 == 1:
        input_data_siswa()
    elif pilih_menu1 == 2:
        for s in siswa:
            print(s)
        input()
    elif pilih_menu1 == 3:
        rekap_kelas()
    elif pilih_menu1 == 4:
        cari_nama = input("Masukan nama: ")
        cari_siswa(cari_nama)
    elif pilih_menu1 == 5:
        cari_nama = input("Masukan nama: ")
        hapus_siswa(cari_nama)
    elif pilih_menu1 == 6:
        break