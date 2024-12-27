import pandas as pd

file_path = 'Dataset Harga Buah dan Sayur.csv'
df = pd.read_csv(file_path)

print("10 Data Pertama:")
print(df.tail(10))

print("\nInformasi Umum Dataset:")
print(df.info())

print("\nStatistik Deskriptif Dataset:")
print(df.describe())

df['year'] = pd.to_datetime(df['date']).dt.year

avg_price_per_year = df.groupby('year')['price'].mean()
print("\nRata-rata Harga Per Tahun:")
print(avg_price_per_year)

max_price = df['price'].max()
min_price = df['price'].min()

max_price_product = df[df['price'] == max_price]
min_price_product = df[df['price'] == min_price]

print("\nProduk dengan Harga Tertinggi:")
print(max_price_product)

print("\nProduk dengan Harga Terendah:")
print(min_price_product)

filtered_products = df[(df['price'] >= 1.50) & (df['price'] <= 2.35)]
print("\nProduk dengan Harga antara 1.50 dan 2.35:")
print(filtered_products)