# TO-DO 1: deklarasi fungsi
def rata_rata(param):
    # TO-DO 2: proses hitung rata-rata
    total_nilai = sum(map(lambda x: x['nilai'], param))  # Mengambil nilai dan menjumlahkan
    rata_rata_nilai = total_nilai / len(param)  # Menghitung rata-rata
    return rata_rata_nilai

# TO-DO 4: panggil fungsi rata_rata() dan tampilkan hasilnya
data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

# Panggil fungsi rata_rata
hasil_rata_rata = rata_rata(data_mahasiswa)

# TO-DO 3: tampilkan hasil rata-rata
print("Rata-rata nilai kelima mahasiswa tersebut adalah: ", hasil_rata_rata)
