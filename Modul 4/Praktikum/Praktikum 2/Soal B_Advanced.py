import math
import time

# Decorator untuk menghitung waktu eksekusi
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Fungsi untuk mengubah input menjadi pasangan titik-titik (x, y)
@execution_time
def map_to_points(input_string):
    try:
        numbers = list(map(int, input_string.split(',')))
        if len(numbers) % 2 != 0:
            raise ValueError("Jumlah angka harus genap.")
        points = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]
        return points
    except ValueError as e:
        print(f"Error: {e}")
        return []

# Fungsi transformasi dengan HOF dan closure
def transform(points):
    def translasi(tx, ty):
        return list(map(lambda p: (p[0] + tx, p[1] + ty), points))
    
    def rotasi(theta):
        rad = math.radians(theta)
        return list(map(lambda p: (
            round(p[0] * math.cos(rad) - p[1] * math.sin(rad), 2),
            round(p[0] * math.sin(rad) + p[1] * math.cos(rad), 2)
        ), points))
    
    def dilatasi(scale):
        return list(map(lambda p: (p[0] * scale, p[1] * scale), points))
    
    return translasi, rotasi, dilatasi

# Fungsi utama untuk mengatur transformasi
@execution_time
def perform_transformations(points):
    translasi, rotasi, dilatasi = transform(points)
    
    # Langkah 1: Translasi
    translated_points = translasi(3, 7)
    print(f"Hasil translasi (tx=3, ty=7): {translated_points}")
    
    # Langkah 2: Rotasi
    rotated_points = rotasi(60)
    print(f"Hasil rotasi (60 derajat): {rotated_points}")
    
    # Langkah 3: Dilatasi
    dilated_points = dilatasi(1.5)
    print(f"Hasil dilatasi (skala=1.5): {dilated_points}")
    
    return translated_points, rotated_points, dilated_points

# Main program
if __name__ == "__main__":
    # Input user
    input_string = input("Masukkan string angka (pisahkan dengan koma): ")
    
    # Map ke titik-titik
    points = map_to_points(input_string)
    if not points:
        exit()
    
    print(f"Titik-titik hasil mapping: {points}")
    
    # Transformasi
    perform_transformations(points)
