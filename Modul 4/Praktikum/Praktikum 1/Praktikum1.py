import time
from functools import reduce

# Decorator untuk menghitung waktu eksekusi
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Mencatat waktu mulai
        result = func(*args, **kwargs)  # Menjalankan fungsi yang dihias
        end_time = time.time()  # Mencatat waktu selesai
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result  # Mengembalikan hasil fungsi
    return wrapper

# Data awal
films = (
    ("Film1", "120 Menit"),
    ("Film2", "150 Menit"),
    ("Film3", "100 Menit")
)

# Fungsi Register
@execution_time
def register(accounts, profiles, transactions):
    nim = input("Masukkan NIM: ")
    if nim in accounts:
        print("Akun dengan NIM ini sudah terdaftar!")
        return accounts, profiles, transactions
    password = input("Masukkan password: ")
    
    accounts[nim] = password
    print("Registrasi berhasil!")
    
    profiles, transactions = create_profile(nim, profiles, transactions)
    return accounts, profiles, transactions

# Fungsi Create Profile menggunakan Closure
def create_profile(nim, profiles, transactions):
    def profile_details():
        name = input("Masukkan nama: ")
        email = input("Masukkan email: ")
        return name, email
    
    name, email = profile_details()
    profiles[nim] = {'name': name, 'email': email}
    transactions[nim] = []
    print("Profil berhasil disimpan!")
    return profiles, transactions

# Fungsi Login
@execution_time
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

# Fungsi untuk melihat profil
@execution_time
def view_profile(nim, profiles, transactions):
    profile = profiles.get(nim, {})
    if not profile:
        print("Profil kosong.")
    else:
        print("Profil:")
        for key, value in profile.items():
            print(f"{key}: {value}")
    view_transactions(nim, transactions)

# Fungsi untuk melihat transaksi
@execution_time
def view_transactions(nim, transactions):
    print("\nDaftar Pesanan Tiket:")
    transaction_list = transactions[nim]
    for i, transaction in enumerate(transaction_list, 1):
        print(f"{i}. Film: {transaction['film']}, Jumlah: {transaction['jumlah']}, Total: {transaction['total']}")

# Fungsi untuk menambahkan pesanan
@execution_time
def add_order(nim, films, transactions):
    print("\nDaftar Film:")
    for i, film in enumerate(films, 1):
        print(f"{i}. {film[0]} ({film[1]})")
    
    choice = int(input("Pilih nomor film yang ingin dipesan: ")) - 1
    if choice < 0 or choice >= len(films):
        print("Pilihan tidak valid!")
        return transactions
    
    jumlah = int(input("Masukkan jumlah tiket: "))
    harga_tiket = 25000
    total = harga_tiket * jumlah
    new_transaction = {'film': films[choice][0], 'jumlah': jumlah, 'total': total}
    transactions[nim].append(new_transaction)
    print(f"Pesanan berhasil! Total harga: {total}")
    return transactions

# Fungsi untuk menghapus pesanan
@execution_time
def delete_order(nim, transactions):
    view_transactions(nim, transactions)
    choice = int(input("Pilih nomor pesanan yang ingin dihapus: ")) - 1
    if choice < 0 or choice >= len(transactions[nim]):
        print("Pilihan tidak valid!")
        return transactions
    
    transactions[nim].pop(choice)
    print("Pesanan berhasil dihapus.")
    return transactions

# Fungsi untuk menghitung total pengeluaran
@execution_time
def calculate_total_spent(transactions):
    return reduce(lambda acc, transaction: acc + transaction['total'], transactions, 0)

# Menu User
@execution_time
def user_menu(nim, films, transactions, profiles):
    while True:
        print("\nUser Menu:")
        print("1. Lihat Profil")
        print("2. Tambah Pesanan Tiket")
        print("3. Hapus Pesanan Tiket")
        print("4. Total Pengeluaran")
        print("5. Keluar")
        
        choice = input("Pilih opsi: ")
        if choice == '1':
            view_profile(nim, profiles, transactions)
        elif choice == '2':
            transactions = add_order(nim, films, transactions)
        elif choice == '3':
            transactions = delete_order(nim, transactions)
        elif choice == '4':
            total = calculate_total_spent(transactions[nim])
            print(f"Total pengeluaran: {total}")
        elif choice == '5':
            break
        else:
            print("Opsi tidak valid!")

# Fungsi Main
def main():
    accounts = {}
    profiles = {}
    transactions = {}
    
    while True:
        print("\nMenu Utama:")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        
        choice = input("Pilih opsi: ")
        if choice == '1':
            accounts, profiles, transactions = register(accounts, profiles, transactions)
        elif choice == '2':
            nim = login(accounts)
            if nim:
                user_menu(nim, films, transactions, profiles)
        elif choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Opsi tidak valid!")

if __name__ == "__main__":
    main()
