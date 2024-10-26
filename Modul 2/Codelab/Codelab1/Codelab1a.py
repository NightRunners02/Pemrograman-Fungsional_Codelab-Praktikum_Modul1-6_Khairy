nilai = [ {'matkul': 'Fungsional', 'nilai': 95},
          {'matkul': 'Mobile', 'nilai': 55} ]

def tambah_nilai(nilai, nama_matkul, jumlah_nilai):
    # Buat salinan dari list 'nilai'
    nilai_baru = [item.copy() for item in nilai]

    # Cari mata kuliah dan update nilai jika ditemukan
    for item in nilai_baru:
        if item['matkul'] == nama_matkul:
            item['nilai'] += jumlah_nilai
            print(f"Nilai {nama_matkul} ditambahkan {jumlah_nilai}. \nTotal nilai {nama_matkul} saat ini {item['nilai']}")
            break
    else:
        print(f"Mata kuliah {nama_matkul} tidak ditemukan dalam daftar!")

    # Kembalikan list baru yang sudah diperbarui
    return nilai_baru

# Panggil fungsi tambah_nilai dengan list 'nilai' sebagai input
nilai_baru = tambah_nilai(nilai, 'Fungsional', 10)

# Cek nilai awal
print("Nilai awal: ", nilai)

# Cek nilai hasil tambah_nilai
print("Nilai update: ", nilai_baru)
