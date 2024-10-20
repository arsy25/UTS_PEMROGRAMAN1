import pyfiglet

teks = "selamat datang"
hasil = pyfiglet.figlet_format(teks)
print(hasil)

#FUNCTION MENENTUKAN KATEGORI NILAI
def tentukan_kategori(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70 and nilai_akhir < 80:
        return "B"
    elif nilai_akhir >= 60 and nilai_akhir < 70:
        return "C"
    elif nilai_akhir >= 50 and nilai_akhir < 60:
        return "D"
    else:
        return "E"

jumlah_mahasiswa = 38
for x in range(1, jumlah_mahasiswa + 1):
    print(f"\n ------ Masukkan data mahasiswa ke-{x} ------")
    # INPUT NILAI TUGAS DAN UAS
    nama = input("masukkan nama mahasiswa : ")
    npm = int(input("masukkan NPM mahasiswa : "))
    nilai_tugas = float(input("masukkan nilai tugas : "))
    nilai_uas = float(input("masukkan nilai uas : "))

    # VALIDASI NILAI YANG VALID
    while nilai_tugas and nilai_uas > 100:
        print("masukkan jumlah nilai yang valid : ")
        nilai_tugas = int(input("masukkan nilai tugas yang valid : "))
        nilai_uas = int(input("masukkan nilai uas yang valid : "))

    # TOTAL KEHADIRAN SELAMA 1 SEMESTER
    total_kehadiran = 16

    # INPUT JUMLAH KEHADIRAN
    jumlah_kehadiran = int(input("masukkan jumlah kehadiran : "))

    # VALIDASI NILAI YANG VALID
    while jumlah_kehadiran > 16:
        print("masukkan jumlah kehadiran yang valid antara 1-16 : ")
        jumlah_kehadiran = int(input("masukkan jumlah kehadiran : "))

# PROSES MENGHITUNG NILAI RATA-RATA DAN PERSENTASE KEHADIRAN
    nilai_ratarata = (nilai_tugas + nilai_uas) / 2
    persentase_kehadiran = (jumlah_kehadiran / total_kehadiran) * 100

# PROSES MENGHITUNG NILAI AKHIR 
    nilai_akhir = nilai_ratarata * (persentase_kehadiran / 100)

    if persentase_kehadiran < 75:
        nilai_akhir = 0
        kategori = tentukan_kategori(nilai_akhir)
        print("Nilai Mutu anda adalah : ", kategori)
        print("Nilai akhir anda adalah : ", nilai_akhir)
    else:
        kategori = tentukan_kategori(nilai_akhir)
        print("Nama anda adalah : ", nama)
        print("NPM anda adalah : ", npm)
        print("Nilai akhir anda adalah : ", nilai_akhir)
        print("Nilai Mutu anda adalah : ", kategori)
        print(f"Persentase kehadiran anda adalah : {persentase_kehadiran}%")




