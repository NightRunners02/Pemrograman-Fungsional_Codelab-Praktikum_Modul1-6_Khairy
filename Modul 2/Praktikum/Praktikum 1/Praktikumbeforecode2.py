# Data Awal (Bioskop)
films = (
    ("Film1", "120 Menit"),
    ("Film2", "150 Menit"),
    ("Film3", "100 Menit")
)

# Database pengguna
accounts = {}  # {'NIM': 'password'}
profiles = {}  # {'NIM': {'name': 'John', 'email': 'john@mail.com'}}
transactions = {}  # {'NIM': [{'film': 'Film1', 'jumlah': 2, 'total': 50000}]}

# Fungsi untuk register
def register():
    nim = input("Masukkan NIM: ")
    if nim in accounts:
        print("Akun dengan NIM ini sudah terdaftar!")
        return
    password = input("Masukkan password: ")

    # Simpan akun
    accounts[nim] = password
    print("Registrasi berhasil!")

    # Menu untuk mengisi profil
    create_profile(nim)

# Fungsi untuk membuat atau mengedit profil
def create_profile(nim):
    name = input("Masukkan nama: ")
    email = input("Masukkan email: ")

    # Simpan profil
    profiles[nim] = {'name': name, 'email': email}
    transactions[nim] = []  # List untuk menyimpan pesanan tiket

    print("Profil berhasil disimpan!")

# Fungsi untuk login
def login():
    nim = input("Masukkan NIM: ")
    if nim not in accounts:
        print("Akun tidak ditemukan!")
        return None

    password = input("Masukkan password: ")
    if accounts[nim] == password:
        print(f"Login berhasil! Selamat datang, {nim}")
        return nim
    else:
        print("Password salah!")
        return None

# Fungsi untuk melihat profil pengguna
def view_profile(nim):
    profile = profiles.get(nim, {})
    if not profile:
        print("Profil kosong.")
    else:
        print("Profil:")
        for key, value in profile.items():
            print(f"{key}: {value}")
    view_transactions(nim)

# Fungsi untuk melihat transaksi pemesanan tiket
def view_transactions(nim):
    print("\nDaftar Pesanan Tiket:")
    for i, transaction in enumerate(transactions[nim], 1):
        print(f"{i}. Film: {transaction['film']}, Jumlah Tiket: {transaction['jumlah']}, Total: {transaction['total']}")

# Fungsi untuk menambah pesanan tiket
def add_order(nim):
    print("\nDaftar Film:")
    for i, film in enumerate(films, 1):
        print(f"{i}. {film[0]} ({film[1]})")

    choice = int(input("Pilih nomor film yang ingin dipesan: ")) - 1
    if choice < 0 or choice >= len(films):
        print("Pilihan tidak valid!")
        return

    jumlah = int(input("Masukkan jumlah tiket: "))
    harga_tiket = 25000  # Harga tiket per film
    total = harga_tiket * jumlah

    # Simpan transaksi
    transactions[nim].append({'film': films[choice][0], 'jumlah': jumlah, 'total': total})
    print(f"Pesanan berhasil! Total harga: {total}")

# Fungsi untuk menghapus pesanan
def delete_order(nim):
    view_transactions(nim)
    choice = int(input("Pilih nomor pesanan yang ingin dihapus: ")) - 1
    if choice < 0 or choice >= len(transactions[nim]):
        print("Pilihan tidak valid!")
        return

    del transactions[nim][choice]
    print("Pesanan berhasil dihapus.")

# Menu pengguna
def user_menu(nim):
    while True:
        print("\nUser Menu:")
        print("1. Lihat profil")
        print("2. Tambah pesanan tiket")
        print("3. Hapus pesanan tiket")
        print("4. Keluar")

        choice = input("Pilih opsi: ")
        if choice == '1':
            view_profile(nim)
        elif choice == '2':
            add_order(nim)
        elif choice == '3':
            delete_order(nim)
        elif choice == '4':
            break
        else:
            print("Opsi tidak valid!")

# Program Utama
while True:
    print("\nMenu Utama:")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")

    menu_choice = input("Pilih opsi: ")

    if menu_choice == '1':
        register()
    elif menu_choice == '2':
        logged_nim = login()
        if logged_nim:
            user_menu(logged_nim)
    elif menu_choice == '3':
        print("Terima kasih!")
        break
    else:
        print("Opsi tidak valid!")
