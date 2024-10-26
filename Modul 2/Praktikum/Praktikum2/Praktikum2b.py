data_penginapan = [
    {"room_id": "GJ123", "cust_name": "Windut", "expenses": 175000, "jumlah_hari": 2, "tanggal": "2024-08-03"},
    {"room_id": "GJ124", "cust_name": "Amonali", "expenses": 120000, "jumlah_hari": 2, "tanggal": "2024-08-03"},
    {"room_id": "GJ125", "cust_name": "Detsit", "expenses": 140000, "jumlah_hari": 4, "tanggal": "2024-08-03"},
    {"room_id": "GJ126", "cust_name": "Bocil Telat", "expenses": 150000, "jumlah_hari": 3, "tanggal": "2024-08-03"},

    {"room_id": "GJ127", "cust_name": "Sandi", "expenses": 160000, "jumlah_hari": 1, "tanggal": "2024-08-04"},
    {"room_id": "GJ128", "cust_name": "Kurnia", "expenses": 135000, "jumlah_hari": 3, "tanggal": "2024-08-04"},
    {"room_id": "GJ129", "cust_name": "Reza", "expenses": 145000, "jumlah_hari": 2, "tanggal": "2024-08-04"},
    {"room_id": "GJ130", "cust_name": "Alya", "expenses": 165000, "jumlah_hari": 1, "tanggal": "2024-08-04"},

    {"room_id": "GJ131", "cust_name": "Bram", "expenses": 200000, "jumlah_hari": 2, "tanggal": "2024-08-05"},
    {"room_id": "GJ132", "cust_name": "Sofi", "expenses": 180000, "jumlah_hari": 1, "tanggal": "2024-08-05"},
    {"room_id": "GJ133", "cust_name": "Dina", "expenses": 170000, "jumlah_hari": 3, "tanggal": "2024-08-05"},
    {"room_id": "GJ134", "cust_name": "Raka", "expenses": 160000, "jumlah_hari": 2, "tanggal": "2024-08-05"}
]

def total_pendapatan():
    tanggal_data = {}

    # Group data by date and calculate total revenue and customers
    for data in data_penginapan:
        tanggal = data['tanggal']
        if tanggal not in tanggal_data:
            tanggal_data[tanggal] = {"total_pendapatan": 0, "jumlah_customer": 0}

        tanggal_data[tanggal]["total_pendapatan"] += data['expenses'] * data['jumlah_hari']
        tanggal_data[tanggal]["jumlah_customer"] += 1

    # Print the results
    for tanggal, info in tanggal_data.items():
        print(f"Tanggal: {tanggal}, Jumlah Customer: {info['jumlah_customer']}, Total Pendapatan: {info['total_pendapatan']}")

# Example usage
total_pendapatan()
