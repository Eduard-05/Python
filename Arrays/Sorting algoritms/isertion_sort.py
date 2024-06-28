array = [3, 2, 8, 1, 7, 9, 4, 6, 5]
min_num = None
position_of_min = None
temporary_int = None

for j in range(len(array)):
    for i in range(j, len(array), 1):
        if min_num == None or min_num > array[i]:
            min_num = array[i]
            position_of_min = i
    array[j], array[position_of_min] = array[position_of_min], array[j]
    min_num = None

print(array)
    
