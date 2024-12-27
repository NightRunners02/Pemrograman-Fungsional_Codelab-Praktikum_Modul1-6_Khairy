import matplotlib.pyplot as plt
import numpy as np

data_matkul = [
    ("Fungsional", 87.5, 48),
    ("Jarkom", 91, 52),
    ("Mobile", 79.7, 40),
    ("Pirdas", 92.5, 49),
    ("Web", 89, 55),
]

mata_kuliah = [x[0] for x in data_matkul]
average_nilai = [x[1] for x in data_matkul]
jumlah_mahasiswa = [x[2] for x in data_matkul]

total_nilai = list(map(lambda x: x[1] * x[2], data_matkul))

print(f"Nama Mata Kuliah: {mata_kuliah}")
print(f"Rata-rata Nilai: {average_nilai}")
print(f"Jumlah Mahasiswa: {jumlah_mahasiswa}")
print(f"Total Nilai: {total_nilai}")

plt.figure(figsize=(18, 12))
plt.subplot(2, 2, 1)
plt.scatter(average_nilai, jumlah_mahasiswa, color='blue', s=100)
plt.title("Scatter Plot: Rata-rata Nilai vs Jumlah Mahasiswa")
plt.xlabel("Rata-rata Nilai")
plt.ylabel("Jumlah Mahasiswa")
for i in range(len(mata_kuliah)):
    plt.text(average_nilai[i], jumlah_mahasiswa[i], mata_kuliah[i], fontsize=9)

plt.subplot(2, 2, 2)
plt.bar(mata_kuliah, total_nilai, color='orange')
plt.title("Diagram Batang: Total Nilai per Mata Kuliah")
plt.xlabel("Mata Kuliah")
plt.ylabel("Total Nilai")
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
plt.plot(mata_kuliah, average_nilai, marker='o', color='green', linestyle='--', linewidth=2)
plt.title("Diagram Garis: Rata-rata Nilai tiap Mata Kuliah")
plt.xlabel("Mata Kuliah")
plt.ylabel("Rata-rata Nilai")

explode = [0.1 if i == jumlah_mahasiswa.index(max(jumlah_mahasiswa)) else 0 for i in range(len(jumlah_mahasiswa))]
plt.subplot(2, 2, 4)
plt.pie(jumlah_mahasiswa, labels=mata_kuliah, explode=explode, autopct='%1.1f%%', shadow=True, colors=plt.cm.Set3.colors)
plt.title("Pie Chart: Distribusi Jumlah Mahasiswa")

plt.tight_layout()
plt.show()
