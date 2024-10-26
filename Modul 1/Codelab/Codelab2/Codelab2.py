def pisahkan_genap_ganjil(input_bilangan):
    list_genap = []  
    list_ganjil = []  
    
    for x in input_bilangan.split():
        bilangan = int(x)  
        if bilangan % 2 == 0:
            list_genap.append(bilangan)  
        else:
            list_ganjil.append(bilangan)  

    return list_genap, tuple(list_ganjil)  

input_bilangan = input("Masukkan beberapa bilangan yang dipisahkan oleh spasi: ")

result_genap, result_ganjil = pisahkan_genap_ganjil(input_bilangan)

print("hasil genap : ", result_genap)
print("hasil ganjil : ", result_ganjil)
