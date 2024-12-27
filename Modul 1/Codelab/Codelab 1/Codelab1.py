floatTuple = []
dataList = []
intDict = {}

random_list = [900, 3.1, 3078, "Hello", 737, "Python", 2.7, 2002, 50,
               "Tech Winter", 7.566, 40, 1, "Is", 60.5, "Better", 1000.1,
               4, "world", 412, 5.5, "AI", 99.234, 12000]

for data in random_list:
    if isinstance(data, float):
        
        floatTuple.append(data)
    elif isinstance(data, str):
        dataList.append(data)    
    elif isinstance(data, int):
        if data < 10:
            intDict[data] = "Satuan"
        elif data < 100:
            intDict[data] = "Puluhan"
        elif data < 1000:
            intDict[data] = "Ratusan"
        elif data >= 1000:
            intDict[data] = "Ribuan"

for key, value in intDict.items(): 
  print(f"{key} : {value}")

print("Float data list =", tuple(floatTuple))
print("String data list =", dataList)
print("Integer data list =", intDict)