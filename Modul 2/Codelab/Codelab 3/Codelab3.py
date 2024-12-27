# TO_DO 1: menerima input tanggal lahir
tanggal_lahir = int(input("Masukkan tanggal lahir (1-31): "))

# TO_DO 2: membuat generator expression
generator_kelipatan = (x for x in range(tanggal_lahir, 1000, tanggal_lahir))

# TO_DO 3: mencetak hasil dalam baris
print("10 data pertama:", end=" ")
for _ in range(10):
    print(next(generator_kelipatan), end=" ")
print()  # untuk memberi baris baru setelah mencetak semua data
