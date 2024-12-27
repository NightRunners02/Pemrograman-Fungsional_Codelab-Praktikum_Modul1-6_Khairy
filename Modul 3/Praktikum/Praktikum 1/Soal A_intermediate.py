from functools import reduce

a_arit = 2  # Suku pertama
d_arit = 3  # Beda (selisih) aritmetika
n = 5       # Jumlah suku

a_geo = 2   # Suku pertama
r_geo = 3   # Rasio geometri

baris_aritmetika = [a_arit + i * d_arit for i in range(n)]

baris_geometri = [a_geo * (r_geo ** i) for i in range(n)]

def jumlahkan(x, y):
    return x + y

jumlah_aritmetika = reduce(jumlahkan, baris_aritmetika)

jumlah_geometri = reduce(jumlahkan, baris_geometri)

print("Barisan aritmetika:", baris_aritmetika)
print("Jumlah barisan aritmetika:", jumlah_aritmetika)
print("Barisan geometri:", baris_geometri)
print("Jumlah barisan geometri:", jumlah_geometri)
