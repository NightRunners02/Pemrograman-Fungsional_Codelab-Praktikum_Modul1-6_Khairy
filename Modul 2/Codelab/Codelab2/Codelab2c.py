# Data mahasiswa asli
data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

# TO_DO 1: deklarasi fungsi generator
def cetak_nilai(param, nim_akhir):
    # TO-DO 2: isi fungsi
    if nim_akhir % 2 == 0:  # NIM genap
        for mahasiswa in param:
            if mahasiswa['nilai'] % 2 == 0:  # Nilai genap
                yield mahasiswa
    else:  # NIM ganjil
        for mahasiswa in param:
            if mahasiswa['nilai'] % 2 != 0:  # Nilai ganjil
                yield mahasiswa

# TO_DO 4: panggil fungsi generator untuk membuat generator object
nim_akhir = 1  # Ganti dengan 0 jika NIM genap
generator_nilai = cetak_nilai(data_mahasiswa, nim_akhir)

# TO_DO 5: menampilkan/print hasil dari generator object
print("Nilai mahasiswa yang sesuai dengan NIM akhir:")
for nilai in generator_nilai:
    print(f"Nama: {nilai['nama']}, Matkul: {nilai['matkul']}, Nilai: {nilai['nilai']}")
