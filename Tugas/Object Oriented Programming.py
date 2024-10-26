class Mobil:
    def __init__(self, warna, tahun):
        self.warna = warna
        self.tahun = tahun

    def tampilkan_info(self):
        print(f"Warna: {self.warna}")
        print(f"Tahun: {self.tahun}")

# Membuat objek dari kelas Mobil
mobil_a = Mobil("Merah", 2020)
mobil_a.tampilkan_info()