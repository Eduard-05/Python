array = []
array2 = []
occurency_of_numbers = []
i = 0
array_size = 0
array_max = None
most_occurred = 0

array_size = int(input("Enter array's size: "))

while i < array_size:
    print("Enter the number: ")
    array.append(int(input()))
    array2.append(array[i])
    i += 1

i = 0

while i < array_size:
    occurency_of_numbers.insert(i, array.count(array2[i]))
    print("occurrence: ", array2[i], " : ", occurency_of_numbers[i])
    i += 1

i = 0

# loop for finding the index of the amount most occurred number

while i < array_size:

    if array_max == None or occurency_of_numbers[i] > array_max:
        array_max = occurency_of_numbers[i]
        most_occurred = array2[i]
    
    i += 1

print(array2)
print("most occured = ", most_occurred)
