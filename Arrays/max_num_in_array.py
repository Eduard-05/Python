array = []
i = 0
array_size = 0
array_max = None

print("enter array size: ")
array_size = int(input())

while i < array_size:
    
    print("enter the number: ")
    array.append(int(input()))
    i += 1

i = 0

while i < array_size:

    if array_max == None or array[i] > array_max:
        array_max = array[i]
    i += 1

print("array max: ", array_max)