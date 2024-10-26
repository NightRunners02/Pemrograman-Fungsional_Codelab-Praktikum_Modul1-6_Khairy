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

def rata_rata_menginap():
    tanggal_data = {}

    # Group customers by date and calculate average
    for data in data_penginapan:
        tanggal = data['tanggal']
        if tanggal not in tanggal_data:
            tanggal_data[tanggal] = []
        tanggal_data[tanggal].append(data['jumlah_hari'])

    # Calculate and print the average
    for tanggal, hari_list in tanggal_data.items():
        rata2 = sum(hari_list) / len(hari_list)
        print(f"Tanggal: {tanggal}, Rata-rata yang menginap: {rata2:.2f}")

# Example usage
rata_rata_menginap()
