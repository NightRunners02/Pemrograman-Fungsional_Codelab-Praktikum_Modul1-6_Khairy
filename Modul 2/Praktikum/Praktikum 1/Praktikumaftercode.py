accounts = {}
profiles = {}
friends_list = {}

def register(accounts):
    nim = input("Masukkan NIM: ")
    if nim in accounts:
        print("Akun dengan NIM ini sudah terdaftar!")
        return accounts
    password = input("Masukkan password: ")

    # Mengembalikan dictionary yang diperbarui
    updated_accounts = {**accounts, nim: password}
    print("Registrasi berhasil!")
    return updated_accounts

def create_profile(nim, profiles, friends_list):
    name = input("Masukkan nama: ")
    role = input("Masukkan peran (user/admin): ")
    email = input("Masukkan email: ")

    # Mengembalikan profile dan friends_list yang diperbarui
    updated_profiles = {**profiles, nim: {'name': name, 'role': role, 'email': email}}
    updated_friends_list = {**friends_list, nim: input("Masukkan daftar teman (pisahkan dengan koma): ").split(',')}

    print("Profil berhasil disimpan!")
    return updated_profiles, updated_friends_list

def login(accounts):
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

def delete_profile(nim, profiles, friends_list):
    updated_profiles = {key: value for key, value in profiles.items() if key != nim}
    updated_friends_list = {key: value for key, value in friends_list.items() if key != nim}
    print("Profil dan daftar teman berhasil dihapus.")
    return updated_profiles, updated_friends_list

while True:
    print("\nMenu Utama:")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")

    menu_choice = input("Pilih opsi: ")

    if menu_choice == '1':
        accounts = register(accounts)
    elif menu_choice == '2':
        logged_nim = login(accounts)
        if logged_nim:
            # Operasikan dengan nim yang sudah login
            while True:
                print("\nUser Menu:")
                print("1. Lihat profil")
                print("2. Edit profil")
                print("3. Hapus profil")
                print("4. Keluar")

                choice = input("Pilih opsi: ")
                if choice == '1':
                    view_profile(logged_nim)
                elif choice == '2':
                    profiles, friends_list = create_profile(logged_nim, profiles, friends_list)
                elif choice == '3':
                    profiles, friends_list = delete_profile(logged_nim, profiles, friends_list)
                elif choice == '4':
                    break
                else:
                    print("Opsi tidak valid!")
    elif menu_choice == '3':
        print("Terima kasih!")
        break
    else:
        print("Opsi tidak valid!")
