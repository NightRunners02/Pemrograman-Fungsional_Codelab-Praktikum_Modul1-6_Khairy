data_mahasiswa = [
    {'nama': 'Karina', 'matkul': 'Pemrograman Fungsional', 'nilai': 90},
    {'nama': 'Seulgi', 'matkul': 'Pemrograman Mobile', 'nilai': 56},
    {'nama': 'Wonyoung', 'matkul': 'Pemrograman Web', 'nilai': 95},
    {'nama': 'Hanni', 'matkul': 'Piranti Cerdas', 'nilai': 88},
    {'nama': 'Jihyo', 'matkul': 'Jaringan Komputer', 'nilai': 63},
]

def hitung_rata_rata(data_mahasiswa):
    total_nilai = 0
    for mahasiswa in data_mahasiswa:
        total_nilai += mahasiswa['nilai']

    rata_rata = total_nilai / len(data_mahasiswa)
    return rata_rata

# Panggil fungsi untuk menghitung rata-rata
rata_rata_nilai = hitung_rata_rata(data_mahasiswa)
print(f"Rata-rata nilai mahasiswa: {rata_rata_nilai}")

def cari_nilai_tertinggi(data_mahasiswa):
    nilai_tertinggi = max(data_mahasiswa, key=lambda x: x['nilai'])
    return nilai_tertinggi

# Panggil fungsi untuk mencari nilai tertinggi
mahasiswa_nilai_tertinggi = cari_nilai_tertinggi(data_mahasiswa)
print(f"Mahasiswa dengan nilai tertinggi: {mahasiswa_nilai_tertinggi['nama']} ({mahasiswa_nilai_tertinggi['nilai']})")

def cari_nilai_terendah(data_mahasiswa):
    nilai_terendah = min(data_mahasiswa, key=lambda x: x['nilai'])
    return nilai_terendah

# Panggil fungsi untuk mencari nilai terendah
mahasiswa_nilai_terendah = cari_nilai_terendah(data_mahasiswa)
print(f"Mahasiswa dengan nilai terendah: {mahasiswa_nilai_terendah['nama']} ({mahasiswa_nilai_terendah['nilai']})")

def kelompokkan_mahasiswa(data_mahasiswa):
    kategori = {'A': [], 'B': [], 'C': [], 'D': []}

    for mahasiswa in data_mahasiswa:
        if mahasiswa['nilai'] >= 85:
            kategori['A'].append(mahasiswa['nama'])
        elif mahasiswa['nilai'] >= 70:
            kategori['B'].append(mahasiswa['nama'])
        elif mahasiswa['nilai'] >= 50:
            kategori['C'].append(mahasiswa['nama'])
        else:
            kategori['D'].append(mahasiswa['nama'])

    return kategori

# Panggil fungsi untuk mengelompokkan mahasiswa
kategori_mahasiswa = kelompokkan_mahasiswa(data_mahasiswa)
print(f"Kategori nilai mahasiswa: {kategori_mahasiswa}")
