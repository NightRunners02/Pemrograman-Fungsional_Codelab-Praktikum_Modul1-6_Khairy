nilai_mahasiswa = {
    "Andi": {"Matematika": 80, "Fisika": 75, "Kimia": 85},
    "Budi": {"Matematika": 70, "Fisika": 65, "Kimia": 75},
    "Citra": {"Matematika": 85, "Fisika": 90, "Kimia": 80},
    "Doni": {"Matematika": 60, "Fisika": 55, "Kimia": 70},
    "Eva": {"Matematika": 95, "Fisika": 85, "Kimia": 90}
}

def rata_rata_per_mahasiswa(nilai_mahasiswa):
    rata_rata_mahasiswa = {}
    for mahasiswa, nilai in nilai_mahasiswa.items():
        total_nilai = sum(nilai.values())
        rata_rata_mahasiswa[mahasiswa] = total_nilai / len(nilai)
    return rata_rata_mahasiswa

def rata_rata_semua_mahasiswa(nilai_mahasiswa):
    total_nilai = 0
    jumlah_nilai = 0
    for nilai in nilai_mahasiswa.values():
        total_nilai += sum(nilai.values())
        jumlah_nilai += len(nilai)
    return total_nilai / jumlah_nilai

rata_mahasiswa = rata_rata_per_mahasiswa(nilai_mahasiswa)
rata_semua_mahasiswa = rata_rata_semua_mahasiswa(nilai_mahasiswa)

print("Rata-rata nilai per mahasiswa:")
for mahasiswa, rata in rata_mahasiswa.items():
    print(f"{mahasiswa}: {rata:.2f}")

print(f"\nRata-rata nilai seluruh mahasiswa: {rata_semua_mahasiswa:.2f}")
