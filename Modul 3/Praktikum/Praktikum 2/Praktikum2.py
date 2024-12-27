from functools import reduce

films = (
    ("Film1", "120 Menit"),
    ("Film2", "150 Menit"),
    ("Film3", "100 Menit")
)

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

def create_profile(nim, profiles, transactions):
    name = input("Masukkan nama: ")
    email = input("Masukkan email: ")

    profiles[nim] = {'name': name, 'email': email}
    transactions[nim] = []

    print("Profil berhasil disimpan!")
    return profiles, transactions

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

def view_profile(nim, profiles, transactions):
    profile = profiles.get(nim, {})
    if not profile:
        print("Profil kosong.")
    else:
        print("Profil:")
        for key, value in profile.items():
            print(f"{key}: {value}")
    view_transactions(nim, transactions)

def view_transactions(nim, transactions):
    print("\nDaftar Pesanan Tiket:")
    transaction_list = transactions[nim]

    formatted_transactions = map(format_transaction, transaction_list)

    for i, transaction in enumerate(formatted_transactions, 1):
        print(transaction)

def format_transaction(transaction):
    return f"Film: {transaction['film']}, Jumlah Tiket: {transaction['jumlah']}, Total: {transaction['total']}"

def list_films(films):
    return [f"{i + 1}. {film[0]} ({film[1]})" for i, film in enumerate(films)]

def add_order(nim, films, transactions):
    print("\nDaftar Film:")
    for film in list_films(films):
        print(film)

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

def delete_order(nim, transactions):
    view_transactions(nim, transactions)
    choice = int(input("Pilih nomor pesanan yang ingin dihapus: ")) - 1
    if choice < 0 or choice >= len(transactions[nim]):
        print("Pilihan tidak valid!")
        return transactions

    transactions[nim] = transactions[nim][:choice] + transactions[nim][choice + 1:]
    print("Pesanan berhasil dihapus.")
    return transactions

def display_transactions_recursive(transactions, index=0):
    if index < len(transactions):
        transaction = transactions[index]
        print(f"{index + 1}. Film: {transaction['film']}, Jumlah Tiket: {transaction['jumlah']}, Total: {transaction['total']}")
        display_transactions_recursive(transactions, index + 1)

def is_above_threshold(transaction, threshold):
    return transaction['total'] > threshold

def filter_transactions_by_total(transactions, threshold):
    return [t for t in transactions if is_above_threshold(t, threshold)]

def sum_totals(acc, transaction):
    return acc + transaction['total']

def calculate_total_spent(transactions):
    return reduce(sum_totals, transactions, 0)

def user_menu(nim, films, transactions, profiles):
    while True:
        print("\nUser Menu:")
        print("1. Lihat profil")
        print("2. Tambah pesanan tiket")
        print("3. Hapus pesanan tiket")
        print("4. Total pengeluaran")
        print("5. Keluar")

        choice = input("Pilih opsi: ")
        if choice == '1':
            view_profile(nim, profiles, transactions)
        elif choice == '2':
            transactions = add_order(nim, films, transactions)
        elif choice == '3':
            transactions = delete_order(nim, transactions)
        elif choice == '4':
            total_spent = calculate_total_spent(transactions[nim])
            print(f"Total pengeluaran: {total_spent}")
        elif choice == '5':
            break
        else:
            print("Opsi tidak valid!")
    return transactions

def main():
    accounts = {}
    profiles = {}
    transactions = {}

    while True:
        print("\nMenu Utama:")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")

        menu_choice = input("Pilih opsi: ")

        if menu_choice == '1':
            accounts, profiles, transactions = register(accounts, profiles, transactions)
        elif menu_choice == '2':
            logged_nim = login(accounts)
            if logged_nim:
                transactions = user_menu(logged_nim, films, transactions, profiles)
        elif menu_choice == '3':
            print("Terima kasih!")
            break
        else:
            print("Opsi tidak valid!")

main()
