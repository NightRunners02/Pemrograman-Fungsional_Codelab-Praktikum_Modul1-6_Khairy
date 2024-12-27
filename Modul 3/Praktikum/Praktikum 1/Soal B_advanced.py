from functools import reduce

def barisan_aritmetika_geometri(a, d, r, n):
    if n == 1:
        return [a]
    else:
        suku_sebelumnya = barisan_aritmetika_geometri(a, d, r, n - 1)
        an = (a + (n - 1) * d) * (r ** (n - 1))
        return suku_sebelumnya + [an]

a = 2  # Suku pertama
d = 3  # Beda (selisih) aritmetika
r = 2  # Rasio geometri
n = 5  # Jumlah suku

hasil = barisan_aritmetika_geometri(a, d, r, n)

def jumlahkan(x, y):
    return x + y

jumlah_arit_geo = reduce(jumlahkan, hasil)

print("Barisan aritmetika-geometri:", hasil)
print("Jumlah barisan aritmetika-geometri:", jumlah_arit_geo)
