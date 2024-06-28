array = [7, 8, 3, 1, 2, 5, 6, 9, 4]
temporary_int = None

for i in range(len(array)):
    temporary_int = array[i]
    for j in range(i, -1, -1):
        if temporary_int < array[j]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)
