array = []
array_size = 0
array_max = None
array_min = None
number = 0
number_index = 0
i = 0

print("Enter array size: ")
array_size = int(input())

print("Enter number you want to find: ")
number = int(input())

while i < array_size:
    
    print("enter the number: ")
    array.append(int(input()))
    i += 1

i = 0

while i < array_size:
    
    if number * 2 == array[i]:
        number_index = i
        print("Index: ", number_index)
    
    i += 1