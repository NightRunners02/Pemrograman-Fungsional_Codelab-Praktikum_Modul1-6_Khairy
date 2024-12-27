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


def cari_customer(nama):
    found = False
    for data in data_penginapan:
        if data['cust_name'].lower() == nama.lower():
            found = True
            total_tagihan = data['expenses'] * data['jumlah_hari']
            print(f"ID Kamar: {data['room_id']}")
            print(f"Tagihan: {data['expenses']}")
            print(f"Jumlah Hari: {data['jumlah_hari']}")
            print(f"Tanggal: {data['tanggal']}")
            print(f"Total Tagihan: {total_tagihan}")
            print("---------------------")

    if not found:
        print(f"Customer dengan nama '{nama}' tidak ditemukan")

# Example usage
cari_customer("Windut")
cari_customer("Sandi")
cari_customer("Bram")
