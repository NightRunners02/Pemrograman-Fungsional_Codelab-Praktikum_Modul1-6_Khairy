import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@execution_time
def input_nilai():
    nilai_input = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")
    nilai_list = list(map(float, nilai_input.split(',')))
    return nilai_list

@execution_time
def hitung_rata_rata(nilai_list):
    rata_rata = sum(nilai_list) / len(nilai_list)
    return rata_rata

@execution_time
def hitung_nilai(nilai_list, rata_rata, nim_genap):
    if nim_genap:
        hasil = list(filter(lambda x: x > rata_rata, nilai_list))
    else:
        hasil = list(filter(lambda x: x < rata_rata, nilai_list))
    return len(hasil)

if __name__ == "__main__":
    nilai_mahasiswa = input_nilai()
    
    rata_rata_nilai = hitung_rata_rata(nilai_mahasiswa)
    print(f"Rata-rata nilai: {rata_rata_nilai:.2f}")
    
    nim_genap = False  
    jumlah_nilai = hitung_nilai(nilai_mahasiswa, rata_rata_nilai, nim_genap)
    
    posisi = "di atas" if nim_genap else "di bawah"
    print(f"Jumlah nilai {posisi} rata-rata: {jumlah_nilai}")
