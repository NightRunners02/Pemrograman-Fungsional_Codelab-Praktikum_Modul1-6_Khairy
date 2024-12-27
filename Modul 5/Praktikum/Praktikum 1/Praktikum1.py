import matplotlib.pyplot as plt
import numpy as np

films = ["Film1", "Film2", "Film3", "Film4"]
orders = [35, 50, 20, 40]
revenue_per_user = [125000, 175000, 50000, 200000, 150000]
users = [f"User{i}" for i in range(1, len(revenue_per_user) + 1)]

plt.figure(figsize=(12, 8))  # Lebar 12, tinggi 8 (dalam inci)

plt.subplot(2, 2, 1)
plt.plot(films, orders, color='blue', linestyle='-', marker='o', label='Pesanan Tiket')
plt.title('Tren Pesanan Tiket')
plt.xlabel('Film')
plt.ylabel('Jumlah Pesanan')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.scatter(users, revenue_per_user, color='green', marker='x', label='Pengeluaran')
plt.title('Distribusi Pengeluaran')
plt.xlabel('Pengguna')
plt.ylabel('Total Pengeluaran')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.subplot(2, 2, (3, 4))
explode = (0, 0.1, 0, 0)
plt.pie(orders, labels=films, explode=explode, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Proporsi Pesanan Tiket')

plt.tight_layout()

plt.show()
