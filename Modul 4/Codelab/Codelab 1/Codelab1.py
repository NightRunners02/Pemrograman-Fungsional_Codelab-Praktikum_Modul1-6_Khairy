from functools import reduce

nilai_mahasiswa = {
    'Zaidun': 99,
    'Suwarsono': 100,
    'Dedi': 75,
    'Joko': 40,
    'Rusdi': 78,
    'Diki': 100,
    'Ansori': 92,
    'Andri': 76,
    'Kahfi': 58,
    'Edi': 77,
    'Joko': 15,
    'Sutadi': 90,
    'Made': 55,
    'Nyoto': 88,
    'Widodo': 100
}

total_nilai = reduce(lambda acc, val: acc + val, nilai_mahasiswa.values())

nilai_tertinggi = reduce(lambda acc, val: acc if acc > val else val, nilai_mahasiswa.values())

mahasiswa_lulus = list(filter(lambda x: nilai_mahasiswa[x] >= 75, nilai_mahasiswa))

nilai_mahasiswa_update = dict(map(
    lambda x: (x[0], x[1] if x[1] >= 75 else x[1] + 5),
    nilai_mahasiswa.items()
))

print("\nHasil Analisis Nilai Mahasiswa:")
print("1. Total Nilai:")
print(f"   - {total_nilai}")

print("2. Nilai Tertinggi:")
print(f"   - {nilai_tertinggi}")

print("3. Mahasiswa yang Lulus (KKM ≥ 75):")
for i, mahasiswa in enumerate(mahasiswa_lulus, start=1):
    print(f"   {i}. {mahasiswa}")

print("4. Nilai Mahasiswa Setelah Update:")
for i, (nama, nilai) in enumerate(nilai_mahasiswa_update.items(), start=1):
    print(f"   {i}. {nama}: {nilai}")
