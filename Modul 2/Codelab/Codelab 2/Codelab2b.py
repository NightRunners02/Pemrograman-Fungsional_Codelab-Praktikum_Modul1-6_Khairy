# TO-DO 1: deklarasi fungsi
def kelulusan(param):
    # TO-DO 2: buat salinan data baru agar tidak merubah data asli (effect-free)
    data_baru = [mahasiswa.copy() for mahasiswa in param]

    # TO-DO 3: ubah data nilai sesuai ketentuan
    for mahasiswa in data_baru:
        if mahasiswa['nilai'] >= 85:
            mahasiswa['nilai'] = 'sempurna'
        elif mahasiswa['nilai'] >= 60:
            mahasiswa['nilai'] = 'memenuhi'
        else:
            mahasiswa['nilai'] = 'gagal'

    # TO-DO 4: output fungsi
    return data_baru

# Data mahasiswa asli
data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

# TO-DO 5: panggil fungsi dan tampilkan hasilnya
hasil_kelulusan = kelulusan(data_mahasiswa)

# Cetak data kelulusan mahasiswa secara vertikal atau per baris
print("Data kelulusan mahasiswa:")
for mahasiswa in hasil_kelulusan:
    print(f"Nama: {mahasiswa['nama']}, Matkul: {mahasiswa['matkul']}, Status Nilai: {mahasiswa['nilai']}")
