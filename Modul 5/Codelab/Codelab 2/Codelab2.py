import pandas as pd

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

nilai_series = pd.Series(nilai_mahasiswa)

print("Series Nilai Mahasiswa:")
print(nilai_series)
