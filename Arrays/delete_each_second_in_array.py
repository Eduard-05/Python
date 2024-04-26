array = []
cutted_array = []
array_length = 0

array_length = int(input("Type array length: "))

for element in range(array_length):
    array.append(int(input("Enter the number: ")))

for element in range(array_length):
    if element % 2 == 0:
        cutted_array.append(array[element])

print(array)
print(cutted_array)
