array = []
i = 0
array_size = 0
array_min = None

print("enter array size: ")
array_size = int(input())

while i < array_size:
    
    print("enter the number: ")
    array.append(int(input()))
    i += 1

i = 0
array_min = array[1]

while i < array_size:

    if array[i] < array_min:
        array_min = array[i]
    i += 1

print("array min: ", array_min)