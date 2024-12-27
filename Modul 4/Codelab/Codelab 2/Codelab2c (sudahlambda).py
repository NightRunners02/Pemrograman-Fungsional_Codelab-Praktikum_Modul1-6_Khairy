from functools import reduce

books = [
    {'judul': 'Pulang', 'penulis': 'Tere Liye', 'halaman': 400},
    {'judul': 'Kapan Nanti', 'penulis': 'Ziggy Z.', 'halaman': 142},
    {'judul': 'Namaku Alam', 'penulis': 'Leila S. Chudori', 'halaman': 448},
    {'judul': 'Origin', 'penulis': 'Dan Brown', 'halaman': 511},
    {'judul': 'Rumah Lebah', 'penulis': 'Ruwi Meita', 'halaman': 288},
    {'judul': 'Kubah', 'penulis': 'Ahmad Tohari', 'halaman': 184},
    {'judul': 'Dompet Ayah Sepatu Ibu', 'penulis': 'J. S. Khairen', 'halaman': 210}
]

buku_awal_k = lambda buku: [b for b in buku if b['judul'].startswith('K')]
ambil_judul = lambda buku: list(map(lambda b: b['judul'], buku))
buku_halaman_lebih_200 = lambda buku: list(filter(lambda b: b['halaman'] > 200, buku))
total_halaman = lambda buku: reduce(lambda total, b: total + b['halaman'], buku, 0)

buku_k = buku_awal_k(books)
judul_buku = ambil_judul(books)
buku_lebih_200 = buku_halaman_lebih_200(books)
total_halaman_buku = total_halaman(books)

print("Buku yang judulnya berawalan huruf 'K':")
for buku in buku_k:
    print(f" - {buku['judul']} oleh {buku['penulis']}, {buku['halaman']} halaman")

print("\nDaftar judul buku:")
for judul in judul_buku:
    print(f" - {judul}")

print("\nBuku dengan halaman lebih dari 200:")
for buku in buku_lebih_200:
    print(f" - {buku['judul']} oleh {buku['penulis']}, {buku['halaman']} halaman")

print(f"\nTotal jumlah halaman semua buku: {total_halaman_buku}")

ambil_penulis = list(map(lambda x: x['penulis'], books))

print(ambil_penulis)
