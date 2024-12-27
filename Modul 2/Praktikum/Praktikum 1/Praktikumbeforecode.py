# Database sederhana
accounts = {}  # Menyimpan NIM dan password
profiles = {}  # Menyimpan profil pengguna
friends_list = {}  # Menyimpan daftar teman pengguna

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

    # Menu untuk melengkapi profil atau skip
    skip = input("Ingin mengisi profil sekarang? (yes/no): ").lower()
    if skip == 'yes':
        create_profile(nim)
    else:
        profiles[nim] = {}  # Profil kosong
        friends_list[nim] = []  # Daftar teman kosong
        print("Profil akan diisi nanti.")

# Fungsi untuk membuat atau mengedit profil
def create_profile(nim):
    name = input("Masukkan nama: ")
    role = input("Masukkan peran (user/admin): ")
    email = input("Masukkan email: ")

    # Simpan profil
    profiles[nim] = {'name': name, 'role': role, 'email': email}

    # Simpan daftar teman
    friends_list[nim] = input("Masukkan daftar teman (pisahkan dengan koma): ").split(',')

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
        print("Profil kosong, silakan isi terlebih dahulu.")
    else:
        print("Profil:")
        for key, value in profile.items():
            print(f"{key}: {value}")
    print(f"Daftar teman: {', '.join(friends_list.get(nim, []))}")

# Fungsi untuk edit profil
def edit_profile(nim):
    print("Edit profil:")
    create_profile(nim)

# Fungsi untuk menghapus profil dan daftar teman
def delete_profile(nim):
    if nim in profiles:
        del profiles[nim]
    if nim in friends_list:
        del friends_list[nim]
    print("Profil dan daftar teman berhasil dihapus.")

# Menu user
def user_menu(nim):
    while True:
        print("\nUser Menu:")
        print("1. Lihat profil")
        print("2. Edit profil")
        print("3. Hapus profil")
        print("4. Keluar")

        choice = input("Pilih opsi: ")
        if choice == '1':
            view_profile(nim)
        elif choice == '2':
            edit_profile(nim)
        elif choice == '3':
            delete_profile(nim)
        elif choice == '4':
            break
        else:
            print("Opsi tidak valid!")

# Main program
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
