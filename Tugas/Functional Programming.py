def tambah(a, b):
    return a + b

def hitung_total_harga(harga_barang):
    return sum(harga_barang)

# Contoh penggunaan fungsi
harga_barang = [10, 20, 30]
total_harga = hitung_total_harga(harga_barang)
print(total_harga)  # Output: 60

# Contoh penggunaan fungsi tambah
hasil_tambah = tambah(2, 3)
print(hasil_tambah)  # Output: 5