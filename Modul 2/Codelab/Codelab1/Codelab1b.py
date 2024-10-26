# TO-DO 1: deklarasi fungsi generator
def cetak_nilai(param):
    # TO-DO 2: loop/iterasi data menggunakan generator
    for item in param:
        # TO-DO 3: output fungsi, menampilkan tiap item
        yield item

# Panggil fungsi cetak_nilai
data_nilai = [{'matkul': 'Fungsional', 'nilai': 95}, {'matkul': 'Mobile', 'nilai': 55}]
nilai_generator = cetak_nilai(data_nilai)  # Generator

# TO-DO 5: tampilkan data/print out generator dengan loop for (NIM ganjil)
print("Output untuk NIM ganjil (dengan loop for):")
for item in nilai_generator:
    print(item)
