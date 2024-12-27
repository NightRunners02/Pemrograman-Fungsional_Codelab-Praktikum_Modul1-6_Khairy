def jumlah_deret_aritmetika(a, d, n):
    if n == 1:
        return a
    else:
        return jumlah_deret_aritmetika(a, d, n - 1) + (a + (n - 1) * d)

a = 2  # Suku pertama
d = 3  # Beda (selisih antar suku)
n = 5  # Jumlah suku

hasil = jumlah_deret_aritmetika(a, d, n)

print("Jumlah deret aritmetika hingga suku ke-", n, "adalah:", hasil)
